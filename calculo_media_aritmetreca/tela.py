from turtle import onclick
import flet as ft
from algoritmo import media


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def medi(e):
        page.clean
        nota1 = float(n.value)
        nota2 = float(n2.value)
        nota3 = float(n3.value)
        nota4 = float(n4.value)

        mediaa = media(nota1, nota2, nota3, nota4)
        page.add(ft.Text(f'A media e de {mediaa}', color=ft.colors.AMBER))

    n = ft.TextField(label='1ª note', width=300)
    n2 = ft.TextField(label='2ª note',width=300)
    n3 = ft.TextField(label='3ª note',width=300)
    n4 = ft.TextField(label='4ª note', width=300)
    btn = ft.ElevatedButton('calcular', on_click=medi)

    page.add(n, n2, n3, n4, btn)

ft.app(main)