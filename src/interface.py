import flet as ft
from flet import Page, ElevatedButton, Text, Column, Row, Container

from process import process_data


def main_interface(page: ft.Page):
    page.title = "Sistema CONFAZ"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 600
    page.window.height = 430
    page.padding = ft.padding.all(10)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    button_width = 500
    text_width = 270

    selected_paths = {
        "month_path": "",
        "confaz_file": ""
    } 
    
    def hide_modal(e=None):
        modal.visible = False
        overlay_bg.visible = False
        page.update()
        
    overlay_bg = ft.Container(
        expand=True,
        bgcolor="#00000080",  # preto com 50% de transparência
        visible=False,
        on_click=hide_modal,
    )
    
    modal = ft.Container(
        content=ft.Column([
            ft.Text("Arquivo atualizado com sucesso!", size=15),
            ft.ElevatedButton("Fechar", on_click=hide_modal)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        width=300,
        height = 100,
        padding=15,
        bgcolor="#FFFFFF",  
        border_radius=10,
        alignment=ft.alignment.center,
        visible=False,
    )
    
    overlay = ft.Stack(
        controls=[
            overlay_bg,
            modal
        ],
        alignment=ft.alignment.center,
        expand=True  # expandir para ocupar toda a área da tela
    )
    
    def show_modal(e=None):
        modal.visible = True
        overlay_bg.visible = True
        page.update()

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    
    def on_result(e: ft.FilePickerResultEvent):
        if e.path:
            selected_paths["month_path"] = e.path
        elif e.files:
            selected_paths["confaz_file"] = e.files[0].path
        page.update()
            
    file_picker.on_result = on_result
    
    def choose_path_month(e):
        file_picker.get_directory_path()

    def choose_path_confaz(e):
        file_picker.pick_files(allow_multiple=False)
        
        
    def update(e):
        if selected_paths["confaz_file"] and selected_paths["month_path"]:
            CONFAZ_MONTH_PATH = selected_paths["month_path"]
            CONFAZ_FILE = selected_paths["confaz_file"]
            MES_ANO = month_name.value
            NEW_CONFAZ_FILE = CONFAZ_FILE.replace(".xlsx", "_ATUALIZADO.xlsx")
            
            process_data(CONFAZ_MONTH_PATH, NEW_CONFAZ_FILE, MES_ANO, CONFAZ_FILE)
            show_modal()
            
        else: 
            error_text.visible = True
            
        page.update()
            
    
    month_name = ft.TextField(
        hint_text= "Informe o mês (xx/20xx)",
        width=text_width
    )
    
    pick_month_button = ft.ElevatedButton(
        "Escolher Pasta do Novo Mês",
        width=button_width,
        on_click=choose_path_month
    )
    pick_confaz_button = ft.ElevatedButton(
        "Escolher Arquivo do CONFAZ",
        width=button_width, 
        on_click=choose_path_confaz
    )
    update_button = ft.Button(
        "Atualizar", 
        width=text_width,
        on_click= update
    )
    
    error_text = ft.Text(
        value="Preencha os campos acima.",
        color="#F44336",
        visible=False
    )
    

    container = ft.Column(
        controls=[
            pick_confaz_button,
            pick_month_button,
            month_name,
            overlay,
            error_text,
            update_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,  
        spacing=20
    )
    
    page.add(container)
