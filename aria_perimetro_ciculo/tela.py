import flet as ft
from algoritmo import calcu


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('Calcular a aria de um circulo', color=ft.colors.AMBER_300, size=30),
        center_title=True
    )


    def calcular(e):
        v_aria = int(valo_araio.value)
        re = calcu (v_aria)

        texto = ft.Text(f'A aria e {re[1]}', color=ft.colors.AMBER_300)
        texto1 = ft.Text(f'Operimitro e {re[0]}', color=ft.colors.AMBER_300)

        page.add(texto, texto1)

    valo_araio = ft.TextField(label='Informe o valor do ario', width=300, label_style=ft.TextStyle(color=ft.colors.BLUE_200))
    btn = ft.ElevatedButton('calcular', on_click=calcular)
    page.add(valo_araio, btn)


ft.app(main)