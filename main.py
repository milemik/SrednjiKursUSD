from usd_to_din import KursVrednost
from get_init_values import get_initial_values
from common import wait_for_user_to_close


def main():
    user_input_value, srednji_kurs = get_initial_values()

    kurs_vrednosti = KursVrednost(user_value=user_input_value, srednji_kurs=srednji_kurs)
    kurs_vrednosti.calculate_value()
    kurs_vrednosti.to_representation()
    wait_for_user_to_close()


if __name__ == "__main__":
    main()
