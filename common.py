def user_input() -> float:
    while True:
        try:
            return float(input("Unesite vasu vrednost u USD dolarima:\n"))
        except (TypeError, ValueError):
            print("Molimo unesite validnu brojcanu vrednost!\nPrimer: 123.34")


def to_representation(uneta_vrednost_u_usd: float, value: float):
    print(f"{uneta_vrednost_u_usd} iznosi {value} dinara")


def wait_for_user_to_close():
    input("PRESS ANY KEY TO CLOSE")
