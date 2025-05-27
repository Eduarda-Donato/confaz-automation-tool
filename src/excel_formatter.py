from openpyxl.styles import Alignment, PatternFill, Border, Side, Font


FILL_YELLOW = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
BORDER_MEDIUM = Border(
    left=Side(style="medium", color="000000"),
    right=Side(style="medium", color="000000"),
    top=Side(style="medium", color="000000"),
    bottom=Side(style="medium", color="000000"),
)
BORDER_THIN = Border(
    left=Side(style="thin", color="000000"),
    right=Side(style="thin", color="000000"),
    top=Side(style="thin", color="000000"),
    bottom=Side(style="thin", color="000000"),
)
BOLD_FONT = Font(name="Calibri", size=11, bold=True)
NORMAL_FONT = Font(name="Arial", size=12)

def format_header(cell):
    cell.fill = FILL_YELLOW
    cell.border = BORDER_MEDIUM
    cell.font = BOLD_FONT
    cell.alignment = Alignment(horizontal="center", vertical="center")
    
def format_data_cell(cell, is_date=False):
    cell.border = BORDER_THIN
    cell.font = NORMAL_FONT
    if is_date:
        cell.number_format = 'DD/MM/YYYY'