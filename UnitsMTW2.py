import flet
from flet import Row, Text, TextButton, Image, Container
from flet import MainAxisAlignment
import json

with open("./units.json", "r", encoding="UTF-8") as file:
    units_json = json.load(file)

def App(page: flet.Page):
    page.title = "Units Medieval Total War 2"
    page.update()

    def mainMenu(e):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        fractions = units_json.get("fractions")

        for id in range(0, len(fractions), 2):
            page.add(
                Row(
                    [
                        TextButton(text=fractions[id].get("fraction_name"), width=200, height=50, on_click=...),
                        TextButton(text=fractions[id + 1].get("fraction_name"), width=200, height=50, on_click=...)
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )

        page.update()

    def unitTypySelectMenu(e, fraction):
        page.controls.clear()
        page.vertical_alignment = MainAxisAlignment.CENTER

        fractions = units_json.get("fractions")

        for id in range(0, len(fractions), 2):
            page.add(
                Row(
                    [
                        TextButton(text=fractions[id].get("fraction_name"), width=200, height=50, on_click=...),
                        TextButton(text=fractions[id + 1].get("fraction_name"), width=200, height=50, on_click=...)
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            )

        page.update()

    mainMenu("e")


if __name__ == '__main__':
    flet.app(App)