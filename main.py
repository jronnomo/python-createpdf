from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_text_color(100,100,10)
    pdf.set_font(family="Helvetica", style="B", size=24)
    pdf.cell(w=0, h=12, txt=f"{df['Topic'][index]}", align="L", ln=1)
    pdf.line(10,21,200, 21)
    for page in range(df["Pages"][index]-1):
        pdf.add_page()

pdf.output("output.pdf")