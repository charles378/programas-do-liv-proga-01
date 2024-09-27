import flet as ft
from algoritmo import qua


def main (page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('A raiz quadrada e o número elevado ao quadrado', color=ft.colors.AMBER_100, size=30),
        center_title=True,
    )


    def somar(e):
        nu = int(num.value)
        raiz = qua(nu)
        texto = ft.Text(f'A raiz quadrada e {raiz[0]}')
        texto1 = ft.Text(f'A o número elevado ao quadrado e {raiz[1]}')

        page.add(texto, texto1)


    num = ft.TextField(label='Informe um número inteiro', width=300,)
    btn = ft.ElevatedButton('somar', on_click=somar)
    page.add(num, btn)


ft.app(main)