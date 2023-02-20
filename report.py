from fpdf import FPDF
import os
page=FPDF()
page.add_page()
page.set_font('Arial', 'B' ,20)
page.cell(50,40, "This is my first pdf report")
page.output('Report.pdf', 'F')
