import flet as ft
import numpy as np
from scipy.linalg import lu
import matplotlib.pyplot as plt
import main

async def main(page: ft.Page):
    page.window_width = 1000
    page.window_height = 1000
    page.window_resizable = False


    matrices=ft.Row([

        ft.Image("Matriz L.png",width=450,height=450),
        ft.Image("Matriz U.png",width=450,height=450)
    ])
    

    col=ft.Column([ft.Image("Matriz.png",width=450,height=450),matrices])
    contenedor= ft.Container(col,width=1000,height=1000,bgcolor=ft.colors.RED_300,alignment=ft.alignment.top_center)
    await page.add_async(contenedor)

ft.app(target=main)
