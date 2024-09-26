import flet as ft
from algoritmo import calc


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('Calcular preço do produto'),
        center_title=True,
        bgcolor=ft.colors.BLACK54,
        actions=[
            
        ]
    )
    
    def calcular(e):
        preço = float(pproduto.value)
        des = float(desconto.value)
        vpagar = calc(preço, des)
        texto = ft.Text(f'O valor a pagar e {vpagar[1]} R$')
        texto1 = ft.Text(f'O valor de desconto e {vpagar[0]} R$')
        page.add(texto, texto1)

    pproduto = ft.TextField(label='Informe o preço do produto', width=300)
    desconto = ft.TextField(label='Imforme o desconto do produto', width=300)
    btn = ft.ElevatedButton('calcular', on_click=calcular)
    page.add(pproduto, desconto, btn)


ft.app(main)