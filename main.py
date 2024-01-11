import math
import json

import flet as ft
import urllib.request

text_for_change = ft.Text(" ")   

def main(page: ft.Page):
    page.title = "MOBILE CHEKER"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 1200
    page.window_height = 800
    def controler1(e):
        value1 = str(txt_number.value)
        if len(value1) == 3:
            txt_number2.focus()
        
    def controler2(e):
        value2 = str(txt_number2.value)
        if len(value2) == 3:
            txt_number3.focus()
    def controler3(e):
        value3 = str(txt_number3.value)
        if len(value3) == 2:
            txt_number4.focus()

    txt_number = ft.TextField(value=None, text_align=ft.TextAlign.CENTER, width=100, max_length=3, on_change=controler1)
    txt_number2 = ft.TextField(value=None, text_align=ft.TextAlign.CENTER, width=100, max_length=3, on_change=controler2)
    txt_number3 = ft.TextField(value=None, text_align=ft.TextAlign.CENTER, width=75, max_length=2, on_change=controler3)
    txt_number4 = ft.TextField(value=None, text_align=ft.TextAlign.CENTER, width=75, max_length=2)

    def get_values(e):
        value1 = txt_number.value
        value2 = txt_number2.value
        value3 = txt_number3.value
        value4 = txt_number4.value
        global phone
        phone = f"7{value1}{value2}{value3}{value4}"
        link = f"https://htmlweb.ru/geo/api.php?json&telcod={phone}"
        try:
            infoPhone = urllib.request.urlopen(link)
            infoPhone = json.load(infoPhone)
            with open(f"info_{phone}.txt", "w") as file:
                file.write(f"Номер сотового -------> +{phone}\n")
                file.write(f"Страна -------> {infoPhone['country']['name']}\n")
                file.write(f"Регион -------> {infoPhone['region']['name']}\n")
                file.write(f"Округ -------> {infoPhone['region']['okrug']}\n")
                file.write(f"Оператор -------> {infoPhone['0']['oper']}\n")
                file.write(f"Часть света -------> {infoPhone['country']['location']}\n")
                text_for_change.value = "- Info in the file -"
                page.update()
        except:
            text_for_change.value = "- The phone not found -"
            page.update()

 

    page.add(
        ft.Row(
            [
                txt_number,
                txt_number2,
                txt_number3,
                txt_number4,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            
        ),
        ft.Row(),
        ft.Row(),
        ft.Row(),
        ft.Row(
            [
                ft.FilledButton(text="Get Info", on_click=get_values, tooltip=100),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
                
        ),
        ft.Row(),
        ft.Row(),
        ft.Row(),
        ft.Row(
            [
                text_for_change
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        
                
    )

ft.app(target=main)