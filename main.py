import flet as ft
import numpy as np
from scipy.linalg import lu
import matplotlib.pyplot as plt



async def main(page:ft.Page):
    page.window_width=720
    page.window_height=1000
    page.window_resizable= False
    global matriz 
    def crear_matriz(n):
        return np.random.randint(-9, 9, size=(n, n))

    def factorizacion_LU(matriz):
        P, L, U = lu(matriz)
        return L, U
    

    async def calcular(e:ft.ContainerTapEvent):
        
        page.update()
        n=int(e.control.value)
        matriz_original = crear_matriz(n)
        matriz_L, matriz_U = factorizacion_LU(matriz_original)
    
        plot_heatmap(matriz_original,"Matriz")
        plot_heatmap(matriz_L,"Matriz L")
        plot_heatmap(matriz_U,"Matriz U")
        matriz_original_text= matriz_a_string(matriz_original)
        matriz_L_text = matriz_a_string(matriz_L)
        matriz_U_text = matriz_a_string(matriz_U)

        matrizn.value = matriz_original_text
        matrizl.value = matriz_L_text
        matrizu.value = matriz_U_text
        t1.value= "Matriz: "
        t2.value= "Matriz L: "
        t3.value= "Matriz U: "
        await page.update_async()
        
        
    def matriz_a_string(matriz):
        matriz_str = ""
        for fila in matriz:
            matriz_str += "["
            for elemento in fila:
                matriz_str += "{:.2f}, ".format(elemento)
            matriz_str = matriz_str[:-2] + "]\n"
        return matriz_str

        
    def plot_heatmap(matriz, title):
        plt.figure(figsize=(6, 6))
        plt.title(title)
        plt.imshow(matriz, cmap='coolwarm', interpolation='nearest')
        for i in range(matriz.shape[0]):
            for j in range(matriz.shape[1]):
                plt.text(j, i, "{:.2f}".format(matriz[i, j]), ha='center', va='center', color='black')
        plt.axis('off')
        plt.savefig(title+'.png')
        


    page.padding=0    
    nxd=120
    titulo = ft.Row([
        ft.Text(value="Factorización LU",size=60),
        ft.Image("upc.png",width=nxd,height=nxd)
    ])

    t1=ft.Text()
    matrizn= ft.Text()
    t2=ft.Text()
    matrizl= ft.Text()
    t3=ft.Text()
    matrizu= ft.Text()
    
    

    def close(e:ft.ContainerTapEvent):
        page.window_destroy()
        print("Hola")

    medtext= ft.Text("Escoja un valor para n del 4 al 10",size=30)


    boton= ft.Container(ft.Text("Ver graficos",size=40,text_align=True),width=250,height=80,on_click=close,border=ft.border.all(),bgcolor=ft.colors.BLACK,border_radius=30,padding=5)

    medidor= ft.Slider(min=2, max=10, divisions=8, label="{value}",on_change_end=calcular)
 
    col = ft.Column(spacing=0,controls=[
        titulo,
        medtext,
        medidor,
        t1,matrizn, 
        t2,matrizl ,
        t3,matrizu,
        boton
        
    ])
    contenedor= ft.Container(col,width=720,height=1280,bgcolor=ft.colors.RED_300,alignment=ft.alignment.top_center)
    
    await page.add_async(contenedor)

   
    

ft.app(target=main)

