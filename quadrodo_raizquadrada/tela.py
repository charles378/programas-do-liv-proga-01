import flet as ft
from algoritmo import raizQua, quadrado


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def calculo(e):
        n = float(num.value)

        quadrad = quadrado(n)
        raiz_quadrada = raizQua(n)

        texto_01 = ft.Text(f'O quadrodo do número {n} e {quadrad}')
        texto_02 = ft.Text(f'A raiz quadrada do número {n} e {raiz_quadrada}')

        page.add(texto_01, texto_02)


    num = ft.TextField(label='Digite um numéro', width=300)
    btn = ft.ElevatedButton('Calcular', on_click=calculo)
    page.add(num, btn)


ft.app(main)