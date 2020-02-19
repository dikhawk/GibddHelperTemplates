#!/usr/bin/python3

import json


def file_to_string(file_name):
    return open("templates/{}".format(file_name)).read()


def save_to_file(file_name, text):
    file = open(file_name, "w")
    file.write(text)
    file.close()


templatesMap = {
    "version": 1,
    "support_app_code_version": 1,
    "templates": [
        {
            "id": "pit_on_road",
            "name": "Яма на дороге",
            "group": "roads",
            "laws_links": [],
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
            "text": file_to_string("pit_on_road")
        },
        {
            "id": "pit_in_yard",
            "group": "roads",
            "name": "Яма во дворе",
            "laws_links": [],
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
            "text": file_to_string("pit_on_yard")
        },
        {
            "id": "parking_on_sidewalk",
            "group": "paprking",
            "name": "Парковка на тротуаре",
            "laws_links": [],
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
            "text": file_to_string("parking_on_sidewalk")
        },
        {
            "id": "parking_in_wrong place",
            "group": "paprking",
            "name": "Парковка в неположенном месте",
            "laws_links": [
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
            "fields": [],
            "text": file_to_string("parking_in_wrong")
        }
    ]
}

save_to_file("Templates.json", json.dumps(templatesMap))
