import flet as ft
from algoritmo import calcu


def main (page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('Horas trabalhada', size=30, color=ft.colors.AMBER_200),
        center_title=True,
    )

    def soma(e):
        ho = float(horasaulas.value)
        quan = int(quantidade_aula.value)
        per = float(percentINSS.value)
        re = calcu(ho, quan, per)
        texto1 = ft.Text(f'O valor do salario bruto e {re[0]} R$')
        texto2 = ft.Text(f'Ovalor do salario liquido e {re[1]} R$')
        page.add(texto1, texto2)

    horasaulas = ft.TextField(label='Valor da horas aula trabalhada', width=300)
    quantidade_aula = ft.TextField(label='Quantidade de aula dadas no mes', width=300)
    percentINSS = ft.TextField(label='qual e o percentual do INSS', width=300)
    btn = ft.ElevatedButton('somar',on_click=soma)

    page.add(horasaulas, quantidade_aula, percentINSS, btn)


ft.app(main)