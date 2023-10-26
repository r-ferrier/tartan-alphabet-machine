from tartan.constants import widths, canvas_width, canvas_height,first_lines_max_width, max_width,key_height, margin, y_tartan_offset, label_gap, colour_key_gap
from tartan.helpers import get_unique_colors, normalize_width
from unidecode import unidecode

# def get_characters_for_width(stripes):
#   stripe_widths = list(set([x['width'] for x in stripes]))
#   characters = {str(x): [] for x in stripe_widths}

#   for stripe in stripes:
#     stripe['letters']
#     characters[str(stripe['width'])] += stripe['letters']

#   print(stripes)

#   return characters

def get_characters_for_width(drawbot, name):
  unique_name = unidecode(name.lower().replace(' ',''))
  return { get_character_width(x,drawbot): [x] for x in unique_name }
   

def get_character_width(char,drawbot):
  return drawbot.textSize(char)[0]

def get_colors_for_character(stripes):
  colors = {}
  for stripe in stripes:
    for letter in stripe['letters']:
      colors[letter] = stripe['color']
  return colors

def get_largest_width(stripe_widths):
  largest_width = 0
  for width in stripe_widths:
    if float(width) > largest_width:
      largest_width = float(width)
  return largest_width

def get_largest_character_width(db, characters):
  largest_width = 0
  for chars in characters:
    width = db.textSize(', '.join(list(set(chars))))[0]
    if largest_width < width:
      largest_width = width
  return largest_width

def draw_horizontal_lines(x1,x2,y,drawbot,count):
  # drawbot.strokeWidth(colour_key_gap/2)
  for i in range(count):
    y_offset = label_gap * (i + 1)
    drawbot.line((x1, y + y_offset),(x2, y + y_offset))
  # drawbot.strokeWidth(1)

def draw_vertical_lines(x,y1,y2,drawbot,count):
  # drawbot.strokeWidth(colour_key_gap/2)
  for i in range(count):
    x_offset = label_gap * (i + 1)
    drawbot.line((x + x_offset, y1),(x + x_offset, y2))
  # drawbot.strokeWidth(1)

def draw_colour_keys(drawbot, colors, x, unique_colors, x_end, colour_width, y):
  for color in colors:
    start_offset = (colour_width / 3) if (color == unique_colors[0]) else (colour_width / 6) if (color == unique_colors[1]) else 0
    end_offset = (colour_width / 2) if (color == unique_colors[0]) else (colour_width / 3) if (color == unique_colors[1]) else (colour_width / 6)
    x1 = x + start_offset + label_gap
    x2 = x + end_offset

    for index, c in enumerate(unique_colors):
      if (color == c):
        draw_horizontal_lines(x1,x2,y,drawbot,index + 1)
        drawbot.line((x, y),(x_end - (index * label_gap * 8), y))


def draw_connecting_lines(drawbot, index, width, colors, unique_colors, x, height, font_size):
  y = (height/(len(unique_colors)))
  y_end_offset = y_tartan_offset - font_size - ( y / 2)
  for color in colors:
    for i, c in enumerate(unique_colors):
      if (color == c):
        drawbot.line(
        (x - (i * 8 * label_gap), y_tartan_offset - (font_size * index)),
        (x + width, y_end_offset - (y * i))
      )
        
def get_number_of_rows(char_list):
  rows = 0
  for c in char_list:
    character_set = list(set(c))
    if(len(character_set)>0):
      rows += 1
  return rows



def draw_colour_grid(drawbot, unique_colors, x, height, font_size):
  
  for i in range(len(unique_colors)+1):
    horizontal_y = y_tartan_offset - font_size - ((height/(len(unique_colors))) * i)
    vertical_x = x + ((height/(len(unique_colors))) * i)
    drawbot.line((x, horizontal_y), (x + height, horizontal_y))
    drawbot.line((vertical_x, y_tartan_offset - font_size), (vertical_x,  y_tartan_offset - font_size - height))
    if i < len(unique_colors):
      draw_horizontal_lines(vertical_x+label_gap,vertical_x+(height/(len(unique_colors)))-label_gap,y_tartan_offset - font_size - height-label_gap*6,drawbot,i+1)
      draw_vertical_lines(x+height+label_gap*2,horizontal_y-label_gap,horizontal_y-(height/(len(unique_colors)))+label_gap,drawbot,i+1)
  

def draw_letters_key(drawbot,stripes, width_divisor,name):
  character_widths = get_characters_for_width(drawbot,name)
  number_of_rows = get_number_of_rows(character_widths.values())
  font_size = key_height/number_of_rows
  drawbot.fontSize(font_size)
  
  color_characters = get_colors_for_character(stripes)
  largest_text_width = get_largest_character_width(drawbot, character_widths.values())
  colour_signifier_width = first_lines_max_width
  text_x_position = margin + normalize_width(get_largest_width(character_widths.keys()),get_largest_width(character_widths.keys())) + (label_gap * 4)
  colour_x_position = text_x_position + largest_text_width + (label_gap * 4)
  colour_width = (colour_signifier_width * 6)-(label_gap * 6)
  colour_x_end_position = colour_x_position + colour_width + (label_gap * 6)
  
  unique_colors = get_unique_colors([x['color'] for x in stripes])
  
  index = 1

  draw_colour_grid(
      drawbot,
      unique_colors,
      colour_x_end_position + colour_signifier_width * 6 + colour_signifier_width,
      (number_of_rows * font_size) - font_size,
      font_size
      )

  for width, characters in character_widths.items():
    normalized_width = normalize_width(float(width),get_largest_width(character_widths.keys()))
    character_set = list(set(characters))
    colors = [color_characters[x] for x in character_set]
    
    if(len(character_set)>0):
      
      drawbot.strokeWidth(0)
      drawbot.text(
        ', '.join(character_set), (
          text_x_position, y_tartan_offset - (font_size * index)
          )
      )
      drawbot.strokeWidth(1)

      drawbot.line(
        (
          margin,
          y_tartan_offset - (font_size * index)
        ),
        (
          margin + normalized_width, 
          y_tartan_offset - (font_size * index)
        )
      )

      draw_colour_keys(
        drawbot, 
        get_unique_colors(colors), 
        colour_x_position,
        unique_colors,
        colour_x_end_position,
        colour_width,
        y_tartan_offset - (font_size * index)
      )

      draw_connecting_lines(
        drawbot,
        index,
        colour_signifier_width * 6,
        get_unique_colors(colors), 
        unique_colors,
        colour_x_end_position,
        (number_of_rows * font_size) - font_size,
        font_size
        )
      
      index += 1
    