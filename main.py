import pandas as pd
import glob
import openpyxl

filepaths = glob.glob("invoices/*xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Excel file has to have some sheet, that we have to specify.
    print(df)