import flet
from flet import Row, Text, TextButton, Image, Container
from flet import MainAxisAlignment
import json

with open("./units.json", "r", encoding="UTF-8") as file:
    units_json = json.load(file)

def getFractionsName() -> list[str]:
    return [units_json.get("fractions")[id].get("fraction_name") for id in range(0, len(units_json.get("fractions")))]

def App(page: flet.Page):
    page.title = "Units Medieval Total War 2"
    page.update()

    def mainMenu(e):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        fractionsName = getFractionsName()

        for id in range(0, len(fractionsName), 2):
            page.add(
                Row(
                    [
                        TextButton(text=fractionsName[id], width=200, height=50, on_click=unitTypySelectMenu(id)),
                        TextButton(text=fractionsName[id+1], width=200, height=50, on_click=unitTypySelectMenu(id+1))
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )

        page.update()

    def unitTypySelectMenu(fractionID: int):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        unitsTypes = list(units_json.get("fractions")[fractionID].get("units").keys())
        print(unitsTypes)

        for id in range(0, len(unitsTypes), 2):
            page.add(
                Row(
                    [
                        TextButton(text=unitsTypes[id].get("unitTypeName"), width=200, height=50, on_click=...),
                        TextButton(text=unitsTypes[id+1].get("unitTypeName"), width=200, height=50, on_click=...)
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )

        page.update()

    mainMenu("e")


if __name__ == '__main__':
    flet.app(App)