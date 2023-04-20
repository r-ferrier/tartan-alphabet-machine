import functools 
from drawBot import *
from tartan.colors import colors, family_colors_1, family_colors_2, family_colors_3, family_colors_5, family_colors_6

napkin_width = 45
bleed = 2
widths = [1,2,3,4,5,9,3]
canvas_unit = napkin_width / 3
canvas_size = napkin_width + (bleed * 2)
max_width = 64
fontSize = 2.25
fontSpacing = 1.5

def draw_tartan(drawbot: drawBotDrawingTools.DrawBotDrawingTool, name_info):
  def draw_name(name,color):
    fontName = drawbot.installFont('./assets/PrincessSofia-Regular.ttf')
    drawbot.fill(*colors[color])
    drawbot.font(fontName, fontSize)
    drawbot.blendMode("normal")
    drawbot.text(name, (fontSpacing + bleed, fontSize + bleed))
    drawbot.blendMode("multiply")
    drawbot.text(name, (fontSpacing + bleed, fontSize + bleed))

  def draw_square(stripes, xOffset, yOffset):

    reversed_stripes = list(reversed(stripes))

    for index, character in enumerate(stripes):
      width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
      reversed_width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in reversed_stripes[0:index+1]])
      width = character['width']
      reversed_width = reversed_stripes[index]['width']      
    
      drawbot.blendMode("multiply")

      drawbot.fill(*character['color'])

      drawbot.rect(xOffset + (width_so_far - width), yOffset, width, canvas_unit * 3)
      drawbot.rect(xOffset + (width_so_far - width) + canvas_unit * 2, yOffset, width,canvas_unit * 3)

      drawbot.rect(xOffset, yOffset + (width_so_far - width), canvas_unit * 3, width )
      drawbot.rect(xOffset, yOffset + (width_so_far - width) + canvas_unit * 2, canvas_unit * 3, width)
      
      drawbot.fill(*reversed_stripes[index]['color'])

      drawbot.rect(xOffset + (reversed_width_so_far - reversed_width) + canvas_unit, yOffset, reversed_width, canvas_unit * 3)
      drawbot.rect(xOffset, yOffset + (reversed_width_so_far - reversed_width) + canvas_unit,canvas_unit * 3,reversed_width)

  def draw_horizontal_flip_square(stripes, xOffset, yOffset):

    reversed_stripes = list(reversed(stripes))

    for index, character in enumerate(stripes):
      width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
      reversed_width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in reversed_stripes[0:index+1]])
      width = character['width']
      reversed_width = reversed_stripes[index]['width']      
    
      drawbot.blendMode("multiply")

      drawbot.fill(*reversed_stripes[index]['color'])

      drawbot.rect(xOffset + (reversed_width_so_far - reversed_width), yOffset, reversed_width, canvas_unit * 3)
      drawbot.rect(xOffset + (reversed_width_so_far - reversed_width) + canvas_unit * 2, yOffset, reversed_width,canvas_unit * 3)
      drawbot.rect(xOffset, yOffset + (reversed_width_so_far - reversed_width) + canvas_unit,canvas_unit * 3,reversed_width)    
      
      drawbot.fill(*character['color'])
      
      drawbot.rect(xOffset + (width_so_far - width) + canvas_unit, yOffset, width, canvas_unit * 3)
      drawbot.rect(xOffset, yOffset + (width_so_far - width), canvas_unit * 3, width )
      drawbot.rect(xOffset, yOffset + (width_so_far - width) + canvas_unit * 2, canvas_unit * 3, width)
      
  def draw_vertical_flip_square(stripes, xOffset, yOffset):

    reversed_stripes = list(reversed(stripes))

    for index, character in enumerate(stripes):
      width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
      reversed_width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in reversed_stripes[0:index+1]])
      width = character['width']
      reversed_width = reversed_stripes[index]['width']      
    
      drawbot.blendMode("multiply")

      drawbot.fill(*reversed_stripes[index]['color'])

      drawbot.rect(xOffset, yOffset + (reversed_width_so_far - reversed_width), canvas_unit * 3, reversed_width )
      drawbot.rect(xOffset, yOffset + (reversed_width_so_far - reversed_width) + canvas_unit * 2, canvas_unit * 3, reversed_width)
      drawbot.rect(xOffset + (reversed_width_so_far - reversed_width) + canvas_unit, yOffset, reversed_width, canvas_unit * 3)
      
      drawbot.fill(*character['color'])

      drawbot.rect(xOffset + (width_so_far - width), yOffset, width, canvas_unit * 3)
      drawbot.rect(xOffset + (width_so_far - width) + canvas_unit * 2, yOffset, width,canvas_unit * 3)
      drawbot.rect(xOffset, yOffset + (reversed_width_so_far - reversed_width) + canvas_unit,canvas_unit * 3,reversed_width)

  def draw_complete_flip_square(stripes, xOffset, yOffset):

    reversed_stripes = list(reversed(stripes))

    for index, character in enumerate(stripes):
      width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
      reversed_width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in reversed_stripes[0:index+1]])
      width = character['width']
      reversed_width = reversed_stripes[index]['width']      
    
      drawbot.blendMode("multiply")

      
      drawbot.fill(*reversed_stripes[index]['color'])

      drawbot.rect(xOffset + (reversed_width_so_far - reversed_width), yOffset, reversed_width, canvas_unit * 3)
      drawbot.rect(xOffset + (reversed_width_so_far - reversed_width) + canvas_unit * 2, yOffset, reversed_width,canvas_unit * 3)

      drawbot.rect(xOffset, yOffset + (reversed_width_so_far - reversed_width), canvas_unit * 3, reversed_width )
      drawbot.rect(xOffset, yOffset + (reversed_width_so_far - reversed_width) + canvas_unit * 2, canvas_unit * 3, reversed_width)
      
      drawbot.fill(*character['color'])

      drawbot.rect(xOffset + (width_so_far - width) + canvas_unit, yOffset, width, canvas_unit * 3)
      drawbot.rect(xOffset, yOffset + (width_so_far - width) + canvas_unit,canvas_unit * 3,width)

  def draw_squares(name_as_stripes_resized):
    draw_square(name_as_stripes_resized,bleed,bleed)
    draw_horizontal_flip_square(name_as_stripes_resized,bleed-napkin_width,bleed)
    draw_horizontal_flip_square(name_as_stripes_resized,bleed+napkin_width,bleed)

    draw_vertical_flip_square(name_as_stripes_resized,bleed,bleed-napkin_width)
    draw_complete_flip_square(name_as_stripes_resized,bleed-napkin_width,bleed-napkin_width)
    draw_complete_flip_square(name_as_stripes_resized,bleed+napkin_width,bleed-napkin_width)

    draw_vertical_flip_square(name_as_stripes_resized,bleed,bleed+napkin_width)
    draw_complete_flip_square(name_as_stripes_resized,bleed-napkin_width,bleed+napkin_width)
    draw_complete_flip_square(name_as_stripes_resized,bleed+napkin_width,bleed+napkin_width)

  drawbot.newPage(canvas_size, canvas_size)
  formatted_name = name_info['name'].lower().split(" ")

  name_for_colors = formatted_name[2] if len(formatted_name) > 2 else formatted_name[1]

  first_name_as_stripes = [{'color': globals()[name_info['colors']](name_for_colors)[(ord(x)-97) % len(globals()[name_info['colors']](name_for_colors))], 'width': widths[(ord(x)-97) % len(widths)]} for x in formatted_name[0]]  
  second_name_as_stripes = [{'color': globals()[name_info['colors']](name_for_colors)[(ord(x)-97) % len(globals()[name_info['colors']](name_for_colors))], 'width': widths[(ord(x)-97) % len(widths)]} for x in formatted_name[1]]  
  
  first_name_width = functools.reduce(lambda a, b: a + b, [x['width'] for x in first_name_as_stripes])
  second_name_width = functools.reduce(lambda a, b: a + b, [x['width'] for x in second_name_as_stripes])
  
  second_name_width_multiplier = (canvas_unit / 2) / second_name_width
  first_name_width_multiplier = (canvas_unit / 2) / first_name_width

  name_as_stripes_resized = [{'color': x['color'], 'width': x['width'] * first_name_width_multiplier} for x in first_name_as_stripes] + [{'color': x['color'], 'width': x['width'] * second_name_width_multiplier} for x in second_name_as_stripes]  

  draw_squares(name_as_stripes_resized)
  draw_name(name_info['initials'],name_info['name_color'])

