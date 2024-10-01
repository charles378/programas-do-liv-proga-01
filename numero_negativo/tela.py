import flet as ft
import algoritmo


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.appbar = ft.AppBar(
        title=ft.Text('contage de número negativo', color=ft.colors.AMBER_200, size=30),
        center_title=True
    )

    def ver(e):
        m = list()
        m.append(int(mun1.value))
        m.append(int(mun2.value))
        m.append(int(mun3.value))
        m.append(int(mun4.value))
        m.append(int(mun5.value))
        
        j = algoritmo.verr(m)
        t = ft.Text(f'a lista inicial {m} tem {len(m)}')
        t1 = ft.Text(f'a lista 2 {j} tem {len(j)} negativo')
        page.add(t, t1)

    mun1 = ft.TextField(label=f'digite o 1ª', width=300)
    mun2 = ft.TextField(label=f'digite o 2ª', width=300)
    mun3 = ft.TextField(label=f'digite o 3ª', width=300)
    mun4 = ft.TextField(label=f'digite o 4ª', width=300)
    mun5 = ft.TextField(label=f'digite o 5ª', width=300)      
    btn = ft.ElevatedButton('ver', on_click=ver)
    page.add(mun1,mun2,mun3,mun4,mun5,btn)


ft.app(main)