from dataclasses import dataclass, field
from typing import List, Optional
from models.entity import Entity
from models.dungeon import Dungeon


@dataclass
class GameState:
    player = None
    dungeon = None
    monsters: List[Entity] = field(default_factory=list)
    items: List[dict] = field(default_factory=list)
    message_log: List[str] = field(default_factory=list)
    turn_counter: int = 0

    def add_message(self, msg):
        self.message_log.append(msg)
        if len(self.message_log) > 50:
            self.message_log.pop(0)