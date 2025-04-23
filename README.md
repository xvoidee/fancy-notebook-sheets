# fancy-notebook-sheets
![Poster](/assets/preview.png)
## What is it?
Generators for various notebook sheets:
* millimeters
* dots

Useful for writing, patterns help with text/drawings positioning and save your money by not buying expensive notebooks from a shop.
## How to use
Install dependencies
```
sudo apt install python3-reportlab
```
Run generator
```
python3 plot.py -h
```
for help and for example to get A4 mm pattern call it like this
```
python3 plot.py -f A4 -p millimeter
```
will produce millimeter_A4.pdf. After that just print your fancy PDFs with B/W settings (I tested it on Brother laser printer only).
