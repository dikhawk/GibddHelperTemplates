#!/usr/bin/python3

import json

version = 2
support_app_code_version = 1

def file_to_string(file_name):
    return open("templates/{}".format(file_name)).read()


def save_to_file(file_name, text):
    file = open(file_name, "w")
    file.write(text)
    file.close()

version_and_support_app_code_version_map = {
    "version": version,
    "support_app_code_version": support_app_code_version
}

templates_map = {
    "version": version,
    "support_app_code_version": support_app_code_version,
    "templates": [
        {
            "id": "general",
            "name": "Общий",
            "group": "",
            "law_links": [

            ],
            "fields": [
            ],
            "text": file_to_string("общий")
        },
        {
            "id": "pit_on_road",
            "name": "Яма на дороге",
            "group": "roads",
            "law_links": [

            ],
            "fields": [
                {
                    "name": "date_time",
                    "hint": "Время и дата нарушения"
                },
                {
                    "name": "location",
                    "hint": "Место расположение ямы"
                },
                {
                    "name": "description",
                    "hint": "Опишите дефект"
                }
            ],
            "text": file_to_string("яма_на_дороге")
        },
        {
            "id": "pit_in_yard",
            "group": "roads",
            "name": "Яма во дворе",
            "law_links": [],
            "fields": [
                {
                    "name": "date_time",
                    "hint": "Время и дата нарушения"
                },
                {
                    "name": "location",
                    "hint": "Место расположение ямы"
                },
                {
                    "name": "description",
                    "hint": "Опишите дефект"
                }
            ],
            "text": file_to_string("яма_во_дворе")
        },
        {
            "id": "parking_on_sidewalk",
            "group": "paprking",
            "name": "Парковка на тротуаре",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "date_time",
                    "hint": "Время и дата нарушения"
                },
                {
                    "name": "location",
                    "hint": "Место расположение ямы"
                },
                {
                    "name": "description",
                    "hint": "Опишите дефект"
                }
            ],
            "text": file_to_string("парковка_на_тротуаре")
        }
    ]
}

save_to_file("templates.json", json.dumps(templates_map))
save_to_file("current_version", json.dumps(version_and_support_app_code_version_map))
