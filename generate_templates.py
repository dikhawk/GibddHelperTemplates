#!/usr/bin/python3

import json
import os

version = 43
support_app_code_version = 20


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
        ###################### GIBDD templates########################
        {
            "id": "general",
            "name": "Общий",
            "type": "gibdd",
            "group": "",
            "description": "",
            "law_links": [

            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место происшествия*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Текст обращения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_общий")
        },
        {
            "id": "pit_on_road",
            "name": "Яма на дороге",
            "type": "gibdd",
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
                    "hint": "Укажите расположения ямы*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Опишите дефект*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_яма_на_дороге")
        },
        {
            "id": "pit_in_yard",
            "name": "Яма во дворе",
            "type": "gibdd",
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
                    "hint": "Укажите расположения ямы*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Опишите дефект*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_яма_во_дворе")
        },
        {
            "id": "parking_on_sidewalk",
            "name": "Парковка на тротуаре",
            "type": "gibdd",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_на_тротуаре")
        },
        {
            "id": "disabled_parking",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка на месте для инвалидов",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_на_месте_для_инвалидов")
        },
        {
            "id": "lawn_parking",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка на газоне",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_на_газоне")
        },
        {
            "id": "pedestrian_parking",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка на пешеходном переходе",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_на_пешеходном_переходе")
        },
        {
            "id": "pedestrian_parking_5metr",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка ближе 5 метров перед пешеходным переходом",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_ближе_5_метров_перед_пешеходным_переходом")
        },
        {
            "id": "prohibited_stop_parking",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка под знаком Остановка запрещена",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_под_знаком_остановка_запрещена")
        },
        {
            "id": "parking_second_row",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка вторым рядом",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_вторым_рядом")
        },
        {
            "id": "parking_on_bus_stop",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля. Сфотографируйте или запишите видео, так чтобы было видно водительское место.",
            "name": "Парковка на остановке общественного транспорта",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_на_остановке_общественного_транспорта")
        },
        {
            "id": "parking_or_driving_on_bike_path",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка или движение по велодорожке или велополосе",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.15. Нарушение правил расположения транспортного средства на проезжей части дороги, встречного разъезда или обгона",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/3616f9cc443dbe11b6898b6fa10d5b67a307cb59/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку, цвет и вид нарушения (двигался по велодорожке, велополосе/припарковался на велодорожке, велополосе)",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_или_движение_по_велодорожке")
        },
        {
            "id": "parking_sidewalk_blocking",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Блокировка прохода на тротуар",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.15. Нарушение правил расположения транспортного средства на проезжей части дороги, встречного разъезда или обгона",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/3616f9cc443dbe11b6898b6fa10d5b67a307cb59/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку, цвет",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_блокировка_прохода_на_тротуар")
        },
        {
            "id": "parking_on_bus_lane",
            "group": "paprking",
            "description": "Делайте фото, так чтобы было видно водительское место. По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Парковка на полосе общественного транспорта",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.16. Несоблюдение требований, предписанных дорожными знаками или разметкой проезжей части дороги",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/423d650543917f5abe5c2480d6fb3fca332f9d22/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку, цвет",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_на_полосе_общественного_транспорта")
        },
        {
            "id": "parking_at_garbage_containers",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля. Сфотографируйте или запишите видео, так чтобы было видно водительское место.",
            "name": "Парковка у мусорных контейнеров",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_у_мусорных_контейнеров")
        },
        {
            "id": "traffic_light_problems",
            "group": "road_infrastructure",
            "description": "",
            "name": "Проблемы со светофором",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.34. Несоблюдение требований по обеспечению безопасности дорожного движения при строительстве, реконструкции, ремонте и содержании дорог, железнодорожных переездов или других дорожных сооружений",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/e6550c7aaf87a7eba570e0dfb5c9d1f86b84298f/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Опишите какой дефект вы обнаружили*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_проблемы_со_светофором")
        },
        {
            "id": "parking_3metrs_from_lane",
            "name": "Парковка ближе 3 метров от полосы",
            "type": "gibdd",
            "group": "paprking",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.19. Нарушение правил остановки или стоянки транспортных средств",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b9c0a2b651b7f06f5693cd2e77f04ff473f50f29/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_парковка_ближе_3_метров_от_полосы")
        },
        {
            "id": "oncoming_traffic_on_oneway_road",
            "group": "roads",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Движение во встречном направлении по дороге с односторонним движением",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.16. Несоблюдение требований, предписанных дорожными знаками или разметкой проезжей части дороги",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/423d650543917f5abe5c2480d6fb3fca332f9d22/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_движение_во_встречном_направлении_по_дороге_с_односторонним_движением")
        },
        {
            "id": "oncoming_traffic_on_road",
            "group": "roads",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Движение по встречке",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.16. Несоблюдение требований, предписанных дорожными знаками или разметкой проезжей части дороги",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/423d650543917f5abe5c2480d6fb3fca332f9d22/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_движение_по_встречке")
        },
        {
            "id": "do_not_provide_an_advantage_at_the_crosswalk",
            "group": "roads",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля.",
            "name": "Не пропустили на пешеходном переходе",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.18. Непредоставление преимущества в движении пешеходам или иным участникам дорожного движения",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/b2daf1d5306cf52a5bb0ec8a1bc0ced772a4f162/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_не_пропустили_на_пешеходном_переходе")
        },
        {
            "id": "blocking_parking",
            "group": "roads",
            "description": "",
            "name": "Установка предметов препятствующих парковке или движению автомобиля",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.33. Повреждение дорог, железнодорожных переездов или других дорожных сооружений",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/370c94c31af735dc73d224582c9f8a9773c89287/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Опишите предмет, который заблокировал парковку*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_установка_предметов_препятствующих_парковке")
        },
        {
            "id": "roadside_driving",
            "group": "roads",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля. Для большей эффективности рекомендуется использовать видео.",
            "name": "Езда по обочине",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.15. Нарушение правил расположения транспортного средства на проезжей части дороги, встречного разъезда или обгона",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/3616f9cc443dbe11b6898b6fa10d5b67a307cb59/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_езда_по_обочине")
        },
        {
            "id": "sidewalk_driving",
            "group": "roads",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля. Для большей эффективности рекомендуется использовать видео. Либо сделать несколько фото, на котором видно движение автомобиля",
            "name": "Езда по тротуару",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.15. Нарушение правил расположения транспортного средства на проезжей части дороги, встречного разъезда или обгона",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/3616f9cc443dbe11b6898b6fa10d5b67a307cb59/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_езда_по_тротуару")
        },
        {
            "id": "abandoned_car",
            "group": "roads",
            "description": "",
            "name": "Бесхозный автомобиль",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "ГК РФ Статья 225. Бесхозяйные вещи",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_5142/9ff952dc782e98c012ec915600891da688cc7bf3/#:~:text=%D0%91%D0%B5%D1%81%D1%85%D0%BE%D0%B7%D1%8F%D0%B9%D0%BD%D1%8B%D0%B5%20%D0%B2%D0%B5%D1%89%D0%B8,-%D0%9F%D0%BE%D0%B7%D0%B8%D1%86%D0%B8%D0%B8%20%D0%B2%D1%8B%D1%81%D1%88%D0%B8%D1%85%20%D1%81%D1%83%D0%B4%D0%BE%D0%B2&text=1.,%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BD%D0%B0%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%83%D1%8E%20%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B8%D0%BA%20%D0%BE%D1%82%D0%BA%D0%B0%D0%B7%D0%B0%D0%BB%D1%81%D1%8F."
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нахождения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку, цвет, как давно припаркован на данном месте*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_брошенный_автомобиль")
        },
        {
            "id": "red_traffic_light",
            "group": "roads",
            "description": "По данному обращению вас могут вызвать в ГИБДД в качестве свидетеля. Для большей эффективности вам стоить отправить видео.",
            "name": "Проезд на красный сигнал светофора",
            "type": "gibdd",
            "law_links": [
                {
                    "title": "КоАП РФ Статья 12.12. Проезд на запрещающий сигнал светофора или на запрещающий жест регулировщика",
                    "link": "http://www.consultant.ru/document/cons_doc_LAW_34661/8e1db11085c966408d1ce0191aef369706a76759/"
                }
            ],
            "fields": [
                {
                    "name": "event_location",
                    "hint": "Укажите место нарушения*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Напишите номер транспортного средства, марку и цвет*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("гибдд_проезд_на_красный_сигнал_светофора")
        },


        ################ Procuracy templates #######################

        {
            "id": "no_answer_from_gibdd_after_30_days",
            "group": "procuracy",
            "description": "Если в течении 30 дней вы не получали уведомлений о продлении срока рассмотрения, или ответ на обращение так и не был получен - это нарушение закона. Согласно ФЗ \"О порядке рассмотрения обращений граждан Российской Федерации\", обращение рассматривается в течение 30 дней со дня регистрации.",
            "name": "Не получен ответ от ГИБДД в течении 30 дней",
            "type": "procuracy",
            "law_links": [
            ],
            "fields": [
                {
                    "name": "procuracy_level_1",
                    "hint": "",
                    "value": "a8f5b01a-0fd8-4989-9249-42851f189878",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "subjects",
                    "hint": "",
                    "value": "b060aa2f-64e2-4c9b-b710-97b582726d8b",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Если хотите, можете добавить свои пояснения",
                    "value": "",
                    "required_field": False,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("прокуратура_не_получен_ответ_от_гибдд_в_течении_30_дней")
        },
        {
            "id": "answer_without_justification",
            "group": "procuracy",
            "description": "ФЗ «О порядке рассмотрения обращений граждан Российской Федерации» сообщает: Государственный орган, орган местного самоуправления или должностное лицо: дает письменный ответ по существу поставленных в обращении вопросов» \nЕсли в ответе:\n1. Не указана дата направления обращения; \n2. Не указаны вопросы, изложенные в обращении, и не даны конкретные ответы о принятых мерах; \n3. Не указан адрес, по которому подано обращение и по которому проведена проверка; \n4. Не указаны факты, по которым проводилась проверка. \nТо это обычная отписка. \nПри заполнении формы вы можете указать пункты подходят под ваш случай.",
            "name": "Немотивированный ответ (Отписка)",
            "type": "procuracy",
            "law_links": [
            ],
            "fields": [
                {
                    "name": "procuracy_level_1",
                    "hint": "",
                    "value": "a8f5b01a-0fd8-4989-9249-42851f189878",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "subjects",
                    "hint": "",
                    "value": "b060aa2f-64e2-4c9b-b710-97b582726d8b",
                    "required_field": True,
                    "visibility": "visible"
                },
                {
                    "name": "appeal_text",
                    "hint": "Укажите перечень допущенных нарушений, которые вашем мнению имеются. См. описание к шаблону.*",
                    "value": "",
                    "required_field": True,
                    "visibility": "visible"
                }
            ],
            "text": file_to_string("прокуратура_немотивированный_ответ")
        },
    ]
}

save_to_file("templates.json", json.dumps(templates_map))
save_to_file("current_version", json.dumps(
    version_and_support_app_code_version_map))
