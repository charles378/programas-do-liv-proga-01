import flet as ft
from algoritmo import somar


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('Calcular a comissão do vendedor', color=ft.colors.AMBER_200, size=30),
        center_title=True,
    )
    

    def calcular(e):
        matricula = maticula.value
        nomee = nome.value
        salario_fix = float(salario_fixo.value)
        total_venda = int(total_vendas.value)
        salario = somar(salario_fix, total_venda)
        texto1 = ft.Text(f'Matricula {matricula}', color=ft.colors.AMBER_200, size=30)
        texto2 = ft.Text(f'Nome {nomee}', color=ft.colors.AMBER_200, size=30)
        texto3 = ft.Text(f'Salario fixo {salario_fix}', color=ft.colors.AMBER_200, size=30)
        texto4 = ft.Text(f'Salario total {salario}', color=ft.colors.AMBER_200, size=30)
        page.add(texto1, texto2, texto3, texto4)

    maticula = ft.TextField(label='Informe a matricula', width=400)
    nome = ft.TextField(label='Nome do colaborador', width=400)
    salario_fixo = ft.TextField(label='O salario fixo do colaborador', width=400)
    total_vendas = ft.TextField(label='O total de vendas', width=400)

    btn = ft.ElevatedButton('calcular', on_click=calcular)

    page.add(maticula, nome, salario_fixo, total_vendas, btn)


ft.app(main)