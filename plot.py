import argparse

from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes

import pattern_dots
import pattern_millimeter

patterns = ['dots', 'millimeter']

paper_formats = {
    'A0'              : {'mm': (841 , 1189), 'inches': (33.1, 46.8)},
    'A1'              : {'mm': (594 , 841 ), 'inches': (23.4, 33.1)},
    'A2'              : {'mm': (420 , 594 ), 'inches': (16.5, 23.4)},
    'A3'              : {'mm': (297 , 420 ), 'inches': (11.7, 16.5)},
    'A4'              : {'mm': (210 , 297 ), 'inches': ( 8.3, 11.7)},
    'A5'              : {'mm': (148 , 210 ), 'inches': ( 5.8,  8.3)},
    'A6'              : {'mm': (105 , 148 ), 'inches': ( 4.1,  5.8)},
    'B0'              : {'mm': (1000, 1414), 'inches': (39.4, 55.7)},
    'B1'              : {'mm': (707 , 1000), 'inches': (27.8, 39.4)},
    'B2'              : {'mm': (500 , 707 ), 'inches': (19.7, 27.8)},
    'B3'              : {'mm': (353 , 500 ), 'inches': (13.9, 19.7)},
    'B4'              : {'mm': (250 , 353 ), 'inches': ( 9.8, 13.9)},
    'B5'              : {'mm': (176 , 250 ), 'inches': ( 6.9,  9.8)},
    'B6'              : {'mm': (125 , 176 ), 'inches': ( 4.9,  6.9)},
    'LETTER'          : {'mm': (216 , 279 ), 'inches': ( 8.5, 11.0)},
    'LEGAL'           : {'mm': (216 , 356 ), 'inches': ( 8.5, 14.0)},
    'ELEVENSEVENTEEN' : {'mm': (432 , 279 ), 'inches': (17.0, 11.0)},
}

def format_dimension(w, h, unit_width=5):
    return f'{str(w).rjust(unit_width)} × {str(h).ljust(unit_width)}'

def get_format_info(fmt):
    fmt = fmt.upper()
    if fmt not in paper_formats:
        print('oops')
        return None
    return paper_formats[fmt]

def print_help():
    print('Available patterns:')
    for p in patterns:
        print(f'    {p}')
    print('\nAvailable paper formats:\n{: <29} {: <14}{}'.format('','mm','inches'))
    for name, sizes in paper_formats.items():
        mm   = format_dimension(*sizes['mm'])
        inch = format_dimension(*sizes['inches'], unit_width=4)
        print(f'    {name:<20} {mm:<16} {inch}')

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--format', type=str,
                    help='Paper format')
parser.add_argument('-l', '--list', action='store_true',
                    help='List available paper formats and patterns')
parser.add_argument('-p', '--pattern', type=str,
                    help='Specify pattern')
args = parser.parse_args()

if args.list:
    print_help()
    exit(0)

if not args.pattern or not args.format:
    parser.error('-p/--pattern and -f/--format are required unless -l/--list is used.')

if args.format not in paper_formats:
    print('Unknown format \'' + args.format + '\'\n')
    print_help()
    exit(0)

if args.pattern not in patterns:
    print('Unknown pattern \'' + args.pattern + '\'\n')
    print_help()
    exit(0)

output                  = args.pattern
page_format             = getattr(pagesizes, args.format, None)
page_width, page_height = page_format

c = canvas.Canvas(args.pattern + '_' + args.format + '.pdf', pagesize = page_format)
if args.pattern == 'millimeter':
    pattern_millimeter.draw(c, page_width, page_height)
if args.pattern == 'dots':
    pattern_dots.draw(c, page_width, page_height)
c.save()

