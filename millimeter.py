from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def grayscale_to_hex(value) -> str:
    return f"#{value:02X}{value:02X}{value:02X}"

def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment

def draw_vertical_line(x):
    c.line(x, 0, x, page_height)

def draw_horizontal_line(y):
    c.line(0, y, page_width, y)

def draw_lines(limit, interval, color, skip, func):
    c.setStrokeColor(color)
    i = -1;
    for x in decimal_range(0, limit, interval):
        i += 1
        if skip != 0 and i % skip == 0:
            continue
        func(x)

inch                    = 2.54
output                  = "millimeter.pdf"

page_width, page_height = A4
page_dpi                = 72

line_color_1mm          = grayscale_to_hex(240)
line_color_5mm          = grayscale_to_hex(230)
line_color_1cm          = grayscale_to_hex(220)

cm_to_points            = page_dpi / inch
line_spacing_1mm        = 0.1 * cm_to_points
line_spacing_5mm        = 0.5 * cm_to_points
line_spacing_1cm        = 1.0 * cm_to_points

c = canvas.Canvas(output, pagesize = A4)

draw_lines(page_height, line_spacing_1mm, line_color_1mm, 5, draw_horizontal_line)
draw_lines(page_width, line_spacing_1mm, line_color_1mm, 5, draw_vertical_line  )

draw_lines(page_height, line_spacing_5mm, line_color_5mm, 0, draw_horizontal_line)
draw_lines(page_width, line_spacing_5mm, line_color_5mm, 0, draw_vertical_line  )

draw_lines(page_height, line_spacing_1cm, line_color_1cm, 0, draw_horizontal_line)
draw_lines(page_width, line_spacing_1cm, line_color_1cm, 0, draw_vertical_line  )

c.save()

