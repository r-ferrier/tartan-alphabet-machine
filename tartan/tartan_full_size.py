import functools 
from drawBot import *
from tartan.colors import colors, family_colors_1, family_colors_2, family_colors_3, family_colors_5, family_colors_6

widths = [1,2,3,4,5,9,3]
canvas_unit = 1000
max_width = 64

def draw_tartan(drawbot: drawBotDrawingTools.DrawBotDrawingTool, name_info, x_offset, y_offset):
  def draw_name(name,color,x_offset,y_offset):
    # fontName = drawbot.installFont('./assets/Cormorant-Medium.ttf')
    fontName = drawbot.installFont('./assets/PrincessSofia-Regular.ttf')
    drawbot.fill(*colors[color])
    drawbot.font(fontName, 150)
    drawbot.blendMode("normal")
    drawbot.text(name, (x_offset + 100, y_offset + 150))
    drawbot.blendMode("multiply")
    drawbot.text(name, (x_offset + 100, y_offset + 150))

  def draw_square(stripes,x_offset,y_offset):

    reversed_stripes = list(reversed(stripes))

    for index, character in enumerate(stripes):
      width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
      reversed_width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in reversed_stripes[0:index+1]])      
    
      drawbot.blendMode("multiply")

      drawbot.fill(*character['color'])
      drawbot.rect(x_offset + ((width_so_far - character['width'])), y_offset + 0,character['width'],canvas_unit * 3)
      drawbot.rect(x_offset + ((width_so_far - character['width'])) + canvas_unit * 2, y_offset + 0,character['width'],canvas_unit * 3)
      drawbot.rect(x_offset + 0, y_offset + ((width_so_far - character['width'])),canvas_unit * 3,character['width'])
      drawbot.rect(x_offset + 0, y_offset + ((width_so_far - character['width']))+canvas_unit * 2,canvas_unit * 3,character['width'])
      
      drawbot.fill(*reversed_stripes[index]['color'])
      drawbot.rect(x_offset + ((reversed_width_so_far - reversed_stripes[index]['width'])) + canvas_unit, y_offset + 0, reversed_stripes[index]['width'], canvas_unit * 3)
      drawbot.rect(x_offset + 0, y_offset + ((reversed_width_so_far - reversed_stripes[index]['width'])) + canvas_unit,canvas_unit * 3,reversed_stripes[index]['width'])
      
  
  formatted_name = name_info['name'].lower().split(" ")

  name_for_colors = formatted_name[2] if len(formatted_name) > 2 else formatted_name[1]

  first_name_as_stripes = [{'color': globals()[name_info['colors']](name_for_colors)[(ord(x)-97) % len(globals()[name_info['colors']](name_for_colors))], 'width': widths[(ord(x)-97) % len(widths)]} for x in formatted_name[0]]  
  second_name_as_stripes = [{'color': globals()[name_info['colors']](name_for_colors)[(ord(x)-97) % len(globals()[name_info['colors']](name_for_colors))], 'width': widths[(ord(x)-97) % len(widths)]} for x in formatted_name[1]]  
  
  first_name_width = functools.reduce(lambda a, b: a + b, [x['width'] for x in first_name_as_stripes])
  second_name_width = functools.reduce(lambda a, b: a + b, [x['width'] for x in second_name_as_stripes])
  
  second_name_width_multiplier = (canvas_unit / 2) / second_name_width
  first_name_width_multiplier = (canvas_unit / 2) / first_name_width

  name_as_stripes_resized = [{'color': x['color'], 'width': x['width'] * first_name_width_multiplier} for x in first_name_as_stripes] + [{'color': x['color'], 'width': x['width'] * second_name_width_multiplier} for x in second_name_as_stripes]  
  # name_as_stripes_resized = [{'color': x['color'], 'width': x['width'] * second_name_width_multiplier} for x in name_as_stripes[:len(formatted_name[1])]]  
  
  draw_square(name_as_stripes_resized,x_offset,y_offset)
  draw_name(name_info['initials'],name_info['name_color'],x_offset,y_offset)

  # colors = [orange,purple,dark_green,pale_pink,dark_blue,hot_pink,pale_blue,yellow]
  # draw_square([{'color': x, 'width': canvas_unit/len(colors)} for x in colors])
