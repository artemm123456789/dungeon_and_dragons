import random

import pygame
import sys
from game_state import GameState
from models.player import Player
from models.dungeon import Dungeon
from systems.map_generator import generate_dungeon
from systems.spawner import spawn_monsters
from systems.battle import melee_attack
from graphics.renderer import Renderer
from dungeon_and_dragons.systems import item_generator


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("Dungeon Crawler")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = GameState()
        self.renderer = Renderer(self.screen, self.state)
        self.initialize()

    def initialize(self):
        matrix, start_x, start_y, rooms = generate_dungeon(width=45, height=20, rooms_count=8)
        self.state.dungeon = Dungeon(matrix=matrix, rooms=rooms)
        self.state.player = Player(
            name="Hero",
            x=start_x, y=start_y,
            hp=30, max_hp=30,
            attack_power=5,
            defense=2,
            next_level_exp=20
        )
        self.state.monsters = spawn_monsters(matrix, count=8)
        self.state.add_message("🔥 Добро пожаловать в Подземелье!")
        self.state.add_message("🗡️ Убей всех монстров, чтобы выбраться.")

    def move_player(self, dx, dy):
        if not self.state.player or not self.state.dungeon:
            return
        player = self.state.player
        new_x = player.x + dx
        new_y = player.y + dy
        matrix = self.state.dungeon.matrix
        if not (0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix)):
            return
        if matrix[new_y][new_x] == 0:
            return
        for monster in self.state.monsters[:]:
            if monster.x == new_x and monster.y == new_y and monster.is_alive:
                log_msg = melee_attack(player, monster)
                self.state.add_message(log_msg)
                if not monster.is_alive:
                    self.state.monsters.remove(monster)
                    self.state.add_message(f"💀 {monster.name} повержен!")
                    if random.randint(1, 100) <= 20:
                        player.get_item(item_generator.generate_random_drop_from_monster(monster.exp))
                self.state.turn_counter += 1
                return
        player.x = new_x
        player.y = new_y
        self.state.turn_counter += 1

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.move_player(0, -1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.move_player(0, 1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.move_player(-1, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.move_player(1, 0)
                elif event.key == pygame.K_SPACE:
                    self.state.add_message("⏳ Ожидание...")
                    self.state.turn_counter += 1

    def run(self):
        while self.running:
            self.handle_events()
            self.renderer.render()  # Отрисовка
            pygame.display.flip()
            self.clock.tick(30)  # 30 FPS
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
