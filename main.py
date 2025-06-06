import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Excel file has to have some sheet, that we have to specify.
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    # ^^^ This gives you the filename 10001-2023.1.18
    invoice_nr = filename.split("-")[0]
    pdf.set_font("Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")