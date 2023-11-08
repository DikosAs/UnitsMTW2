import flet
from flet import Row, TextButton, Image, Container, Text
from flet import MainAxisAlignment, colors, border_radius
import json

with open("./units.json", "r", encoding="UTF-8") as file:
    units_json = json.load(file)

def getFractionsName() -> list[str]:
    return list(units_json.get("fractions").keys())

def getFractionUnitTypesName(fractionName: str) -> list[str]:
    return list(units_json.get("fractions").get(fractionName).get("units").keys())

def getUnitsName_forFractionAndTypes(fractionName: str, unitTypeName: str) -> list[str]:
    return list(units_json.get("fractions").get(fractionName).get("units").get(unitTypeName))

def getUnitInfo(fractionName: str, unitTypeName: str, unitName: str) -> dict:
    print(dict(units_json.get("fractions").get(fractionName).get("units").get(unitTypeName).get(unitName)))
    return dict(units_json.get("fractions").get(fractionName).get("units").get(unitTypeName).get(unitName))

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
                        TextButton(text=fractionsName[id], width=200, height=50, on_click=unitTypySelectMenu, data=fractionsName[id]),
                        TextButton(text=fractionsName[id+1], width=200, height=50, on_click=unitTypySelectMenu, data=fractionsName[id+1])
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )

        page.update()

    def unitTypySelectMenu(e):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        unitsTypes = getFractionUnitTypesName(e.control.data)

        for id in range(0, len(unitsTypes), 2):
            page.add(
                Row(
                    [
                        TextButton(text=unitsTypes[id], width=200, height=50, on_click=unitSelectMenu, data=(e.control.data, unitsTypes[id])),
                        TextButton(text=unitsTypes[id+1], width=200, height=50, on_click=unitSelectMenu, data=(e.control.data, unitsTypes[id+1]))
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )

        page.update()

    def unitSelectMenu(e):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        data = e.control.data
        units = getUnitsName_forFractionAndTypes(data[0], data[1])

        for id in range(0, len(units), 2):
            page.add(
                Row(
                    [
                        TextButton(text=units[id], width=200, height=50, on_click=unitMenu, data=(data[0], data[1], units[id])),
                        TextButton(text=units[id + 1], width=200, height=50, on_click=unitMenu, data=(data[0], data[1], units[id+1]))
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )

        page.update()

    def unitMenu(e):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        data = e.control.data
        unit_info = getUnitInfo(data[0], data[1], data[2])

        page.add(

            )
        )

    mainMenu("e")

if __name__ == '__main__':
    flet.app(App)