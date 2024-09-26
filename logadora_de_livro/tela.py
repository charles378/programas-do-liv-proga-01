import flet as ft
from algoritmo import  loga


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('Valor de locaçao de livros', color=ft.colors.AMBER_200, size=30),
        center_title=True
    )


    def calc(e):
        q = int(qlivros.value)
        v = float(valuguel.value)
        soma = loga(q, v)
        texto1 =ft.Text(f'O faturamento mensal e {soma[0]} R$')
        texto2 = ft.Text(f'O faturamento anual considerando a locaçao de 80% dos livros e {soma[1]} R$')
        page.add(texto1, texto2)

    qlivros = ft.TextField(label='Informe a contidade de livros ', width=300)
    valuguel = ft.TextField(label='Informe o valor do aluguel',width=300)
    btn = ft.ElevatedButton('calcular', on_click=calc)

    page.add(qlivros, valuguel, btn)


ft.app(main)