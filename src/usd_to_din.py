from dataclasses import dataclass


@dataclass
class KursVrednost:
    user_value: float
    srednji_kurs: float
    calculated_value: float = 0.0

    def calculate_value(self) -> float:
        self.calculated_value = self.srednji_kurs * self.user_value

    def to_representation(self):
        print(f"{self.user_value} iznosi {self.calculated_value} dinara")
