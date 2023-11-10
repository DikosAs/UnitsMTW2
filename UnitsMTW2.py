import flet
from flet import Row, TextButton, Image, Column, Text
from flet import MainAxisAlignment
import json

with open("units.json", "r", encoding="UTF-8") as file:
    units_json = json.load(file)

def getFractionsName() -> list[str]:
    return list(units_json.keys())

def getFractionUnitTypesName(fractionName: str) -> list[str]:
    return list(units_json.get(fractionName).keys())

def getUnitsName_forFractionAndTypes(fractionName: str, unitTypeName: str) -> list[str]:
    return list(units_json.get(fractionName).get(unitTypeName))

def getUnitInfo(fractionName: str, unitTypeName: str, unitName: str) -> dict:
    return dict(units_json.get(fractionName).get(unitTypeName).get(unitName))

def App(page: flet.Page):
    page.title = "Units Medieval Total War 2"
    page.update()

    def mainMenu(e):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        fractionsName = getFractionsName()

        for id in range(0, len(fractionsName), 2):
            try:
                page.add(
                    Row(
                        [
                            TextButton(text=fractionsName[id], width=200, height=50, on_click=unitTypySelectMenu, data=fractionsName[id]),
                            TextButton(text=fractionsName[id+1], width=200, height=50, on_click=unitTypySelectMenu, data=fractionsName[id+1])
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                )
            except:
                page.add(
                    Row(
                        [
                            TextButton(text=fractionsName[id], width=200, height=50, on_click=unitTypySelectMenu, data=fractionsName[id])
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
            try:
                page.add(
                    Row(
                        [
                            TextButton(text=unitsTypes[id], width=200, height=50, on_click=unitSelectMenu, data=(e.control.data, unitsTypes[id])),
                            TextButton(text=unitsTypes[id+1], width=200, height=50, on_click=unitSelectMenu, data=(e.control.data, unitsTypes[id]))
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                )
            except:
                page.add(
                    Row(
                        [
                            TextButton(text=unitsTypes[id], width=400, height=50, on_click=unitSelectMenu, data=(e.control.data, unitsTypes[id]))
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                )

        page.add(
            Row(
                [
                    TextButton(text="Назад", width=400, height=50, on_click=mainMenu)
                ],
                alignment=MainAxisAlignment.CENTER
            )
        )


        page.update()

    def unitSelectMenu(e):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER
        page.update()

        data = e.control.data
        units = getUnitsName_forFractionAndTypes(data[0], data[1])

        for id in range(0, len(units), 2):
            try:
                page.add(
                    Row(
                        [
                            TextButton(text=units[id], width=200, height=50, on_click=unitMenu, data=(data[0], data[1], units[id])),
                            TextButton(text=units[id + 1], width=200, height=50, on_click=unitMenu, data=(data[0], data[1], units[id+1]))
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                )
            except:
                page.add(
                    Row(
                        [
                            TextButton(text=units[id], width=200, height=50, on_click=unitMenu, data=(data[0], data[1], units[id]))
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                )
        page.add(
            Row(
                [
                    TextButton(text="Назад", width=400, height=50, on_click=unitTypySelectMenu, data=data[0])
                ],
                alignment=MainAxisAlignment.CENTER
            )
        )


        page.update()

    def unitMenu(e):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        def newWin(e):
            flet.app(App)

        data = e.control.data
        unit_info = getUnitInfo(data[0], data[1], data[2])
        page.add(
            Column(
                [
                    Row(
                        [
                            Image(src=unit_info.get("image"))
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    Row(
                        [
                            Column(
                                [
                                    Text(unit_info.get("specifications").get("primary_weaponName"), width=200),
                                    Text(f'Атрибут: {unit_info.get("specifications").get("primary_weaponAttributes") if unit_info.get("specifications").get("primary_weaponAttributes") != "" else "Нету"}', width=200, height=25),
                                    Text(f'Атака: {unit_info.get("specifications").get("primary_attack")}', width=200),
                                    Text(f'Бонусы: {unit_info.get("specifications").get("primary_bonus")}', width=200),
                                    Text(f''),
                                    Text(f'Тотальная защита: {unit_info.get("specifications").get("totalDefence")}'),
                                    Text(f'Броня: {unit_info.get("specifications").get("arm")}'),
                                    Text(f'Навык защиты: {unit_info.get("specifications").get("defSkill")}')
                                ],
                                alignment=MainAxisAlignment.CENTER
                            ),
                            Column(
                                [
                                    Text(unit_info.get("specifications").get("secondary_weaponName") if unit_info.get("specifications").get("secondary_weaponName") != "" else "Второе оружие отсутствует", width=200, height=25),
                                    Text(f'Атрибут: {unit_info.get("specifications").get("secondary_weaponAttributes") if unit_info.get("specifications").get("secondary_weaponAttributes") != "" else "Нету"}', width=200),
                                    Text(f'Атака: {unit_info.get("specifications").get("secondary_attack")}', width=200),
                                    Text(f'Бонусы: {unit_info.get("specifications").get("secondary_bonus")}', width=200),
                                    Text(f''),
                                    Text(f'Щит: {unit_info.get("specifications").get("shield")}'),
                                    Text(f'Здоровье: {unit_info.get("specifications").get("health")}'),
                                    Text(f'')
                                ],
                                alignment=MainAxisAlignment.CENTER
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    Row(
                        [
                            Text(unit_info.get("description") if unit_info.get("description") != "" else "Описание отсутствует", width=410)
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    Row(
                        [
                            TextButton("Сравнить", width=200, on_click=newWin),
                            TextButton("Назад", width=200, on_click=unitSelectMenu, data=(data[0], data[1]))
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                ],
                alignment=MainAxisAlignment.CENTER
            )
        )

        page.update()

    mainMenu("e")

if __name__ == '__main__':
    flet.app(target=App)