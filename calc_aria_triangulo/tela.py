import flet as ft
from algoritmo import calcuaria


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor =ft.colors.BLUE_900


    def calcular(e):
        ba = float(base.value)
        al = float(altura.value)
        aria = calcuaria(ba, al)
        texto1 = ft.Text(f'A aria do triângulo e {aria}', size=30)
        page.add(texto1)


    btn = ft.ElevatedButton('calcular', on_click=calcular)
    base = ft.TextField(label='informe a base do triângulo', width=300)
    altura = ft.TextField(label='informe a altura do triângulo', width=300)
    page.add(base, altura, btn)


ft.app(main)