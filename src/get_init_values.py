import requests
from bs4 import BeautifulSoup as bs
from common import user_input


URL = "https://nbs.rs/kursnaListaModul/srednjiKurs.faces?lang=cir&style=layout.css"


class GetInitialValues:
    def __init__(self) -> None:
        self.soup: bs = None
        self.tr_elements: list = []
        self.user_input: float = 0.0
        self.srednji_kurs: float = 0.0

    def send_request_to_nbs(self) -> bs:
        response = requests.get(URL)
        self.soup = bs(response.text, "html.parser")

    def check_response(self) -> list:
        self.all_tr = self.soup.find_all("tr")
        if len(self.all_tr) < 30:
            raise "PROBLEM"

    def get_usd_course(self) -> float:
        for tr in self.all_tr:
            if "USD" in tr.text:
                self.srednji_kurs = zz_get_usd_value(data_td=tr.find_all("td"))
                break
        return self.srednji_kurs

    def print_current_usd_value(self) -> None:
        print(f"DANASNJI KURS DOLARA: {self.srednji_kurs}")

    def get_current_usd_value(self) -> float:
        self.send_request_to_nbs()
        self.check_response()
        srednji_kurs = self.get_usd_course()
        self.print_current_usd_value()
        return srednji_kurs


def zz_get_usd_value(data_td) -> float:
    data = [data.text for data in data_td]
    return float(data[-1].replace(",", "."))


def get_initial_values():
    srednji_kurs = GetInitialValues().get_current_usd_value()
    user_input_value = user_input()
    return user_input_value, srednji_kurs
