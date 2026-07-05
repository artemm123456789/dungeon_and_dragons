import pygame
from graphics.colors import COLORS


class Renderer:
    def __init__(self, screen, game_state):
        self.screen = screen
        self.state = game_state
        self.tile_size = 20  # Размер одного тайла в пикселях

    def render(self):
        self.screen.fill((0, 0, 0))  # Заливка экрана черным фоном

        # 1. Рисуем карту
        dungeon = self.state.dungeon
        if dungeon:
            # dungeon.matrix - это будет матрица с нулями и единицами, если 0 - то это стена, используем цвет COLORS['wall'], если 1 - то это пол, цвет COLORS['floor']
            # нам надо пройти по всей матрице и нарисовать прямоугольнички.
            # для их рисования используем следующую строку
            # pygame.draw.rect(self.screen, твой_цвет, [x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size])


        # 2. Рисуем монстров
        # self.state.monsters - это список с монстрами. Надо проверить, жив ли монстр (monster.is_alive хранит значение True или False), и если жив - нарисовать его в виде круга
        # круг рисуется так
        # pygame.draw.circle(self.screen, COLORS['monster'], [координаты центра по x, координаты центра по y, радиус)
        #



        # 3. Рисуем игрока
        if self.state.player:
            # узнаем координаты x и y игрока и рисуем круг на его месте



        # 4. Панель статов (простой текст)
        font = pygame.font.SysFont(None, 24)
        if self.state.player:
            stats_text = # здесь в переменную stats_text нужно сохранить единую строку, в которой будет хп персонажа (текущее и максимальное), атака и защита
            surface = font.render(stats_text, True, (255, 255, 255))
            self.screen.blit(surface, (10, 10))



        # 5. Лог (последние 3 сообщения)
        if self.state.message_log:
            log_font = pygame.font.SysFont(None, 20)
            messages = self.state.message_log[-3:]
            for i, msg in enumerate(messages):
                surf = log_font.render(msg, True, (200, 200, 200))
                self.screen.blit(surf, (10, self.screen.get_height() - 60 + i * 20))