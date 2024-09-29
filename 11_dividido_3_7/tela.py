import flet as ft
from algoritmo import somar


def main (page: ft.Page):


    def calcular(e):
        nume = int(num.value)
        resut =  somar(nume)
        texto2 = ft.Text(f'O {nume} {resut} e divizivel por 3 e 7', color=ft.colors.AMBER_200, size=30)
        page.add(texto2)

    num = ft.TextField(label='Informe um número', width=300)
    btn = ft.ElevatedButton('calcular', on_click=calcular)
    page.add(num, btn)


ft.app(main)