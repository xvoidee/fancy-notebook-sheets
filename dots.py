from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def grayscale_to_hex(value) -> str:
    return f"#{value:02X}{value:02X}{value:02X}"

def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment

def draw_lines(limit, interval, color, skip, func):
    c.setStrokeColor(color)
    i = -1;
    for x in decimal_range(0, limit, interval):
        i += 1
        if skip != 0 and i % skip == 0:
            continue
        func(x)

inch                    = 2.54
output                  = "dots.pdf"

page_width, page_height = A4
page_dpi                = 72

cm_to_points            = page_dpi / inch
dot_color               = grayscale_to_hex(220)
dot_spacing             = 0.5 * cm_to_points
dot_radius              = 0.5

c = canvas.Canvas(output, pagesize = A4)
c.setStrokeColor(dot_color)
c.setFillColor  (dot_color)

for y in decimal_range(0, page_height, dot_spacing):
    for x in decimal_range(0, page_width, dot_spacing):
        c.circle(x, y, dot_radius)

c.save()

