from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_text_color(100,100,10)
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)

    pdf.line(10,21,200, 21)
    pdf.ln(263)
    pdf.set_text_color(180,180,200)
    pdf.set_font(family="Times", style="I", size=10)

    pdf.cell(0, 10, txt=row["Topic"], align="R")
    for page in range(df["Pages"][index]-1):
        pdf.add_page()
        pdf.ln(275)
        pdf.set_text_color(180, 180, 200)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.cell(0, 10, txt=row["Topic"], align="R")

pdf.output("output.pdf")