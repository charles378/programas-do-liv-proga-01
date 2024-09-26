import flet as ft
from algoritmo import antec,suces


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def antece(e):
        n = int(num.value)
        nn = antec(n)
        texto = ft.Text(f'O antecessor e {nn}')
        page.add(texto)


    def suce(e):
        n = int(num.value)
        nn = suces(n)
        texto = ft.Text(f'O sucessor e {nn}')
        page.add(texto)


    num = ft.TextField(label='Qual e o número')
    leb = ft.Row(controls=[ft.ElevatedButton('Antecessor', on_click=antece), ft.ElevatedButton('Sucessor', on_click=suce)])
    
    page.add(num, leb)



ft.app(main)