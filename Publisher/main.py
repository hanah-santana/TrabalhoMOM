import flet as ft
from Publicador import UnityType, PublisherData

def main(page: ft.Page):
    sensorList = []
    def validade(e):
        if all([input_text.value, drop_down.value]):
            submit_button.disabled = False
        else:
            submit_button.disabled = True
        page.update()
            
    def submit(e):
        if input_text.value in sensorList:
            page.snack_bar.content = ft.Text("Já existe um sensor com esse ID")
            page.snack_bar.open = True
        else:
            sensorList.append(input_text.value)
            PublisherData(drop_down.value, input_text.value, range_slider.start_value, range_slider.end_value)
            print(drop_down.value)
            page.snack_bar.content = ft.Text("Seu sensor foi criado com sucesso!")
            page.snack_bar.open = True
        page.update()
        
    page.title = "Publicador"
    page.horizontal_alignment = "CENTER"
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Seu sensor foi criado com sucesso!"),
        action="Ok!",
    )
    page.window.width = 800
    page.window.height = 350
    page.window.resizable = False
    page.vertical_alignment = "CENTER"
    page.horizontal_alignment = "CENTER"
    page.theme = ft.Theme(color_scheme_seed=ft.colors.GREEN_200)
    page.bgcolor = ft.colors.BROWN_400


    input_text = ft.TextField( label="ID Sensor", hint_text="Digite o ID do sensor", on_change=validade)
    submit_button = ft.ElevatedButton(text="Criar sensor", on_click=submit, style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(10)))

    range_slider = ft.RangeSlider(
        min=-200,
        max=200,
        divisions=400,
        start_value=0,
        end_value=100,
        label='{value}',
        width=350,
    )
    drop_down = ft.Dropdown(
        label="Tipo de dado",
        options=[
            ft.dropdown.Option(UnityType.velocity.value, text=UnityType.velocity.value),
            ft.dropdown.Option(UnityType.umidity.value, text=UnityType.umidity.value),
            ft.dropdown.Option(UnityType.temperature.value, text=UnityType.temperature.value),
            ],
        )
    range_slider_label = ft.Text((str(range_slider.start_value) + " ~ " + str(range_slider.end_value)), size=16)
    def slider_label_change(e):
        range_slider_label.value = str(int(range_slider.start_value)) + " ~ " + str(int(range_slider.end_value))
        page.update()
    range_slider.on_change = slider_label_change
    
    submit_button.disabled = True
    input_text.on_change = validade
    drop_down.on_change = validade

    page.add(
        ft.Row([input_text, drop_down], alignment="Center"),
        ft.Card(content=ft.Row([range_slider_label], alignment="CENTER"), width=150, color=ft.colors.BROWN_700),
        ft.Column([range_slider, submit_button], horizontal_alignment="CENTER")
        )
ft.app(main)
