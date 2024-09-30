import flet as ft
import algoritmo


def main(page: ft.Page):
    lista = []


    def ver(e):
        num = int(mun.value)
        m = algoritmo.ver(num)
        page.add(ft.Text(f'o {m}'))

    for c in range(0,5):
        mun = ft.TextField(label=f'digite o {c + 1}ª')
        lista.append(mun)
        
        page.add(mun)
    btn = ft.ElevatedButton('ver', on_click=ver)
    page.add(btn)


ft.app(main)