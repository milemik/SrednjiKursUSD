from dataclasses import dataclass
from decimal import ROUND_DOWN, Decimal


@dataclass
class KursVrednost:
    user_value: float
    srednji_kurs: float
    calculated_value: float = 0.0

    def calculate_value(self) -> float:
        calculated_curs_value = self.srednji_kurs * self.user_value
        self.calculated_value =  Decimal(calculated_curs_value).quantize(Decimal('.001'))

    def to_representation(self):
        print(f"{self.user_value} iznosi {self.calculated_value} dinara")
