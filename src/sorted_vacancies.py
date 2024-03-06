import json
from datetime import datetime
from config import FILE
from pprint import pprint


class SortedVacancy:
    def __init__(self):
        self.head_hunter_sorted = []
        self.date_format = None

    @property
    def sorted_vacancies_hh(self):
        with open(FILE, encoding="utf-8") as file:
            content = json.load(file)
        for i in content["items"]:
            if i["salary"]["from"] is None:
                i["salary"]["from"] = 0
            if i["salary"]["to"] is None:
                i["salary"]["to"] = 0
            if i["published_at"]:
                date = datetime.strptime(i["published_at"], "%Y-%m-%dT%H:%M:%S+%f")
                self.date_format = f"{date:%d.%m.%Y}"
            self.head_hunter_sorted.append({
                "name": i["name"],
                "city": i["area"]["name"],
                "payment_1": i["salary"]["from"],
                "payment_2": i["salary"]["to"],
                "skill_1": i["snippet"]["requirement"],
                "skill_2": i["snippet"]["responsibility"],
                "date": self.date_format
            })
        return self.head_hunter_sorted


if __name__ == '__main__':
    r = SortedVacancy()
    pprint(r.sorted_vacancies_hh)
    