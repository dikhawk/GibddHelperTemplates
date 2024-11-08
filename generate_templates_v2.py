#!/usr/bin/python3

import os
from dataclasses import dataclass
from enum import Enum
import xml.etree.ElementTree as ET
import json


TEMPLATES_DIRECTORY = "templates"
PATH_TO_TEMPLATES_JSON = "templates.json"
PATH_TO_CURRENT_VERSION_JSON = "current_version"
VERSION = 47
SUPPORT_APP_CODE_VERSION = 20


class Visibility(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"


@dataclass
class LawLink:
    title: str
    link: str


@dataclass
class Field:
    name: str
    hint: str
    value: str
    required_field: bool
    visibility: str


@dataclass
class Template:
    id: str
    name: str
    type: str
    group: str
    description: str
    law_links: list[LawLink]
    fields: list[Field]
    text: str


@dataclass
class TemplatesResponse:
    version: int
    support_app_code_version: int
    templates: list[Template]


@dataclass
class CurrentVersion:
    version: int
    support_app_code_version: int


def generate_templates() -> list[Template]:
    templates: list[Template] = []

    types_of_templates = os.listdir(TEMPLATES_DIRECTORY)

    for type in types_of_templates:
        path_to_type = f"{TEMPLATES_DIRECTORY}{os.sep}{type}"

        if os.path.isfile(path_to_type):
            print(f"{path_to_type} is not a directory")
            continue

        groups = os.listdir(path_to_type)

        for group in groups:
            path_to_group = f"{TEMPLATES_DIRECTORY}{os.sep}{type}{os.sep}{group}"
            if os.path.isfile(path_to_type):
                print(f"Type: {path_to_type} is not a directory")
                continue

            templatesFiles = os.listdir(path_to_group)

            for templateFile in templatesFiles:
                template = get_template(type=type, group=group, fileName=templateFile)

                if template is not None:
                    templates.append(template)

    return templates


def get_template(type: str, group: str, fileName: str) -> Template:
    path_to_template = (
        f"{TEMPLATES_DIRECTORY}{os.sep}{type}{os.sep}{group}{os.sep}{fileName}"
    )

    if "*" in fileName:
        print(f"Template is ignored: {path_to_template}")
        return None

    if os.path.isdir(path_to_template):
        print(f"Template: {path_to_template} is not a file")

        return None

    if not (is_valid_template_xml(path_to_template)):
        raise SyntaxError("Invalid template file format")

    return parse_template_xml(type=type, group=group, path_to_file=path_to_template)


def file_as_string(path_to_file: str) -> str:
    if not (os.path.exists(path_to_file)):
        print(f"File does not exist: {path_to_file}")
        return None
    return open(path_to_file).read()


def parse_template_xml(type: str, group: str, path_to_file) -> Template:
    if not (os.path.exists(path_to_file)):
        print(f"File does not exist: {path_to_file}")
        return None

    element: ET.Element = ET.parse(path_to_file).getroot()

    return Template(
        id=element.find("id").text,
        name=element.find("name").text,
        type=type,
        group=group,
        description=element.find("description").text,
        law_links=parse_law_links(element.find("law_links")),
        fields=parse_fields_xml(element.find("fields")),
        text=element.find("text").text,
    )


def parse_fields_xml(fields_element: ET.Element) -> list[Field]:
    result: list[Field] = []

    for field in fields_element.findall("field"):
        result.append(
            Field(
                name=field.find("name").text,
                hint=field.find("hint").text,
                value=field.find("value").text,
                required_field=(
                    True if field.find("required_field").text == "true" else False
                ),
                visibility=field.find("visibility").text,
            )
        )

    return result


def parse_law_links(links_element: ET.Element) -> list[LawLink]:
    result: list[LawLink] = []

    for link in links_element.findall("link"):
        result.append(
            LawLink(
                title=link.find("title").text,
                link=link.find("link").text,
            )
        )

    return result


def template_to_dict(template: Template) -> dict:
    templateAsDict = template.__dict__
    templateAsDict["fields"] = [field.__dict__ for field in template.fields]
    templateAsDict["law_links"] = [law_link.__dict__ for law_link in template.law_links]

    return templateAsDict


def generate_json_response(templates: list[Template]) -> str:
    current_version: CurrentVersion = get_current_version()
    response = TemplatesResponse(
        version=current_version.version,
        support_app_code_version=current_version.support_app_code_version,
        templates=[template_to_dict(template) for template in templates],
    )
    return json.dumps(response.__dict__)


def is_valid_template_xml(path_to_file: str) -> bool:
    element: ET.Element = ET.parse(path_to_file).getroot()

    if element.find("id") is None:
        return False

    if element.find("name") is None:
        return False

    if element.find("description") is None:
        return False

    if element.find("law_links") is None:
        return False

    if element.find("fields") is None:
        return False

    if element.find("text") is None:
        return False

    return True


def save_to_file(file_name, text):
    file = open(file_name, "w")
    file.write(text)
    file.close()


def update_current_version_if_have_changes():
    if not (os.path.exists(PATH_TO_CURRENT_VERSION_JSON)):
        save_to_file(
            PATH_TO_CURRENT_VERSION_JSON,
            json.dumps(
                CurrentVersion(
                    support_app_code_version=SUPPORT_APP_CODE_VERSION, version=VERSION
                ).__dict__
            ),
        )
        return

    templates_json = generate_json_response(generate_templates())
    previous_templates_json = open(PATH_TO_TEMPLATES_JSON, encoding="utf-8").read()

    if previous_templates_json != templates_json:
        current_version: CurrentVersion = get_current_version()
        current_version.version = current_version.version + 1

        save_to_file(PATH_TO_CURRENT_VERSION_JSON, json.dumps(current_version.__dict__))

    print()


def get_current_version() -> CurrentVersion:
    current_version_json = json.loads(
        open(PATH_TO_CURRENT_VERSION_JSON, encoding="utf-8").read()
    )
    return CurrentVersion(
        version=current_version_json["version"],
        support_app_code_version=current_version_json["support_app_code_version"],
    )

def check_repeated_template_id(templates: list[Template]):
    ids: set[str] = set()
    
    for template in templates:
        if template.id in ids:
            raise IndexError(f"Repeated id: {template.id}")
        
        ids.add(template.id)
    return

def main():
    templates: list[Template] = generate_templates()
    check_repeated_template_id(templates)
    update_current_version_if_have_changes()

    response_json = generate_json_response(templates)
    save_to_file(PATH_TO_TEMPLATES_JSON, response_json)


main()
