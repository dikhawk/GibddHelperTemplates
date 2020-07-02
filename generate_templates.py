#!/usr/bin/python3

import json
import os

version = 11
support_app_code_version = 1


def file_to_string(file_name):
    return open("{}/templates/{}".format(os.path.dirname(__file__), file_name)).read()


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
            "description": "",
            "law_links": [

            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место прооисшествия*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Текст обращения*"
                }
            ],
            "text": file_to_string("общий")
        },
        {
            "id": "pit_on_road",
            "name": "Яма на дороге",
            "group": "roads",
            "description": "",
            "law_links": [
                {
                    "title": "ГОСТ Р 50597-2017. Национальный стандарт Российской Федерации.",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_285670/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите расположения ямы*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Опишите дефект*"
                }
            ],
            "text": file_to_string("яма_на_дороге")
        },
        {
            "id": "pit_in_yard",
            "group": "roads",
            "description": "",
            "name": "Яма во дворе",
            "law_links": [
                {
                    "title": "ГОСТ Р 50597-2017. Национальный стандарт Российской Федерации.",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_285670/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите расположения ямы*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Опишите дефект*"
                }
            ],
            "text": file_to_string("яма_во_дворе")
        },
        {
            "id": "parking_on_sidewalk",
            "group": "paprking",
            "description": "",
            "name": "Парковка на тротуаре",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*"
                }
            ],
            "text": file_to_string("парковка_на_тротуаре")
        },
        {
            "id": "disabled_parking",
            "group": "paprking",
            "description": "По данному обращению вас могу вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка на месте для инвалидов",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*"
                }
            ],
            "text": file_to_string("парковка_на_месте_для_инвалидов")
        },
        {
            "id": "disabled_parking",
            "group": "paprking",
            "description": "По данному обращению вас могу вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка на месте для инвалидов",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*"
                }
            ],
            "text": file_to_string("парковка_на_месте_для_инвалидов")
        },
        {
            "id": "lawn_parking",
            "group": "paprking",
            "description": "По данному обращению вас могу вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка на газоне",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*"
                }
            ],
            "text": file_to_string("парковка_на_газоне")
        },
        {
            "id": "pedestrian_parking",
            "group": "paprking",
            "description": "По данному обращению вас могу вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка на пешеходном переходе",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*"
                }
            ],
            "text": file_to_string("парковка_на_пешеходном_переходе")
        },
        {
            "id": "prohibited_stop_parking",
            "group": "paprking",
            "description": "По данному обращению вас могу вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка под знаком Остановка запрещена",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*"
                }
            ],
            "text": file_to_string("парковка_под_знаком_остановка_запрещена")
        },
        {
            "id": "traffic_light_problems",
            "group": "road_infrastructure",
            "description": "",
            "name": "Проблемы со светофором",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.34. Несоблюдение требований по обеспечению безопасности дорожного движения при строительстве, реконструкции, ремонте и содержании дорог, железнодорожных переездов или других дорожных сооружений",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/e6550c7aaf87a7eba570e0dfb5c9d1f86b84298f/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Опишите какой дефект вы обнаружили*"
                }
            ],
            "text": file_to_string("проблемы_со_светофором")
        },
        {
            "id": "oncoming_traffic_on_oneway_road",
            "group": "roads",
            "description": "По данному обращению вас могу вызвать в ГИБДД в качестве свидетеля.",
            "name": "Движение во встречном направлении по дороге с односторонним движением",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.16. Несоблюдение требований, предписанных дорожными знаками или разметкой проезжей части дороги",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/423d650543917f5abe5c2480d6fb3fca332f9d22/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*"
                }
            ],
            "text": file_to_string("движение_во_встречном_направлении_по_дороге_с_односторонним_движением")
        },
        {
            "id": "do_not_provide_an_advantage_at_the_crosswalk",
            "group": "roads",
            "description": "По данному обращению вас могу вызвать в ГИБДД в качестве свидетеля.",
            "name": "Не пропустили на пешеходном переходе",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.18. Непредоставление преимущества в движении пешеходам или иным участникам дорожного движения",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b2daf1d5306cf52a5bb0ec8a1bc0ced772a4f162/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*"
                }
            ],
            "text": file_to_string("не_пропустили_на_пешеходном_переходе")
        }
    ]
}

save_to_file("templates.json", json.dumps(templates_map))
save_to_file("current_version", json.dumps(
    version_and_support_app_code_version_map))
