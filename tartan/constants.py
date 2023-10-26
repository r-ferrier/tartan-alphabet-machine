#NAPKINS

widths = [1,2,3,4,5,9,3]
canvas_width = 2970
canvas_height = 4200
max_width = 64
margin = 600
y_tartan_offset = canvas_height - canvas_width
label_gap = 8
fontSize = 102
colour_key_gap = 8
key_height = 6 * fontSize
first_lines_max_width = 100

# Colour in sheets

outlined_args = {
  "A5": 
  {
    "margin": 150, 
    "raw_canvas_width": 1485, 
    "raw_canvas_height": 2100,
    "font_size": 64,
    "title_offset": 0,
    "label_gap": 6,
    "colour_signifier_width": 50
  },
  "A4": 
  {
    "margin": 150, 
    "raw_canvas_width": 2100, 
    "raw_canvas_height": 2970,
    "font_size": 88,
    "title_offset": 20,
    "label_gap": 8,
    "colour_signifier_width": 75
  },
  "A3": 
  {
    "margin": 200, 
    "raw_canvas_width": 2970, 
    "raw_canvas_height": 4200,
    "font_size": 120,
    "title_offset": 40,
    "label_gap": 10,
    "colour_signifier_width": 100
  }
}