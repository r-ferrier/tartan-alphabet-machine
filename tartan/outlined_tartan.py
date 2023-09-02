import functools 
from drawBot import *
from tartan.colors import colors, family_colors_1, family_colors_2, family_colors_3, family_colors_5, family_colors_6, family_colors_7

widths = [1,2,3,4,5,9,3]
canvas_unit = 1000
max_width = 64
margin = 100
label_gap = 8
fontSize = 32

def draw_outlined_tartan(drawbot: drawBotDrawingTools.DrawBotDrawingTool, name_info):

  def name_without_letters(stripes):
    return [ {
      'color': x['color'], 
      'letters': [], 
      'width': x['width'],
      'is_end_of_name': True
    } for x in stripes]

  def combine_stripes(stripe, next_stripe):
    new_stripes = {'stripes': [stripe, next_stripe], 'is_combined': False}
    if stripe['color'] == next_stripe['color']:
      new_stripes = {
        'stripe': {
          'color': stripe['color'], 
          'letters': stripe['letters'] + next_stripe['letters'], 
          'width': stripe['width'] + next_stripe['width'],
          'is_end_of_name': next_stripe['is_end_of_name']
          }, 
        'is_combined': True
      }
    return new_stripes
  
  def get_combined_stripes(all_stripes):
    for index, stripe in enumerate(all_stripes):
      if index < len(all_stripes) - 1:
        result = combine_stripes(stripe, all_stripes[ index + 1 ])
        if result['is_combined']:
          all_stripes[index] = result['stripe']
          del all_stripes[index + 1]
          get_combined_stripes(all_stripes)
          break
    return all_stripes
  
  def get_unique_colors(colors):
    new_colors = []
    for color in colors:
      if color not in new_colors:
        new_colors.append(color)
    return new_colors

  
  def draw_square(stripes):
    fontName = drawbot.installFont('./assets/VT323-Regular.ttf')
    drawbot.stroke(0,0,0)
    drawbot.fill(1,1,1,0)
    drawbot.font(fontName, fontSize)

    colors = get_unique_colors([x['color'] for x in stripes])

    for index, character in enumerate(stripes):
      width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
        
      drawbot.rect((margin + (width_so_far - character['width'])),margin,character['width'],canvas_unit * 3)
      drawbot.rect(margin, margin + ((width_so_far - character['width'])),canvas_unit * 3,character['width'])
    
      horizontal_y = (margin / 2) if (len(character['letters']) > 0) else (margin / 1.25)
      drawbot.line(((margin + (width_so_far - character['width'])) + (label_gap / 2), horizontal_y),((((margin + (width_so_far - character['width'])) + character['width'])-(label_gap/2)),horizontal_y))
      drawbot.line((margin/1.25, (margin + (width_so_far - character['width'])) + (label_gap/2)),(margin/1.25, (((margin + (width_so_far - character['width'])) + character['width'])-(label_gap/2))))

      if(len(colors) > 1 and character['color'] == colors[0]):
        horizontal_y = (margin / 2.5) if (len(character['letters']) > 0) else (margin / 1.42857142857)
        drawbot.line(((margin + (width_so_far - character['width'])) + (label_gap / 2),horizontal_y),((((margin + (width_so_far - character['width'])) + character['width'])-(label_gap/2)),horizontal_y))
        drawbot.line((margin/1.42857142857, (margin + (width_so_far - character['width'])) + (label_gap / 2)),(margin / 1.42857142857, (((margin + (width_so_far - character['width'])) + character['width'])-(label_gap / 2))))
      
      if (len(colors) > 2 and character['color'] == colors[1]):
        horizontal_y = (margin / 2.5) if (len(character['letters']) > 0) else (margin / 1.42857142857)
        drawbot.line(((margin + (width_so_far - character['width'])) + (label_gap / 2),horizontal_y),((((margin + (width_so_far - character['width'])) + character['width'])-(label_gap/2)),horizontal_y))   
        horizontal_y = (margin / 3.333333) if (len(character['letters']) > 0) else (margin / 1.66666666667)
        drawbot.line(((margin + (width_so_far - character['width'])) + (label_gap / 2),horizontal_y),((((margin + (width_so_far - character['width'])) + character['width'])-(label_gap/2)),horizontal_y))
        drawbot.line((margin/1.42857142857, (margin + (width_so_far - character['width'])) + (label_gap / 2)),(margin / 1.42857142857, (((margin + (width_so_far - character['width'])) + character['width'])-(label_gap / 2))))
        drawbot.line((margin/1.66666666667, (margin + (width_so_far - character['width'])) + (label_gap / 2)),(margin / 1.66666666667, (((margin + (width_so_far - character['width'])) + character['width'])-(label_gap / 2))))
      
      drawbot.fill(0,0,0)
      drawbot.stroke(0,0,0,0)
      for index, letter in enumerate(character['letters']):
        number_of_letters = len(character['letters']) * 2 if character['is_end_of_name'] else len(character['letters'])
        x_start = (margin + (width_so_far - character['width'])) - (fontSize / 4)
        width = character['width']
        letter_width = width / (number_of_letters + (2 if character['is_end_of_name'] else 1))
        drawbot.text(letter, ((x_start + (letter_width * (index+1))), margin/1.5))
      
      drawbot.stroke(0,0,0)
      drawbot.fill(1,1,1,0)
      
    drawbot.rect(margin, margin, canvas_unit * 3, canvas_unit * 3)  

  drawbot.newPage(3 * canvas_unit + margin * 2, 3 * canvas_unit + margin * 2)
  formatted_name = name_info['name'].lower().split(" ")

  name_for_colors = formatted_name[2] if len(formatted_name) > 2 else formatted_name[1]

  first_name_as_stripes = [
    {
      'color': globals()[name_info['colors']](name_for_colors)[(ord(x)-97) % len(globals()[name_info['colors']](name_for_colors))], 
      'width': widths[(ord(x)-97) % len(widths)],
      'letter': x
    } for x in formatted_name[0]
  ]  
  second_name_as_stripes = [
    {
      'color': globals()[name_info['colors']](name_for_colors)[(ord(x)-97) % len(globals()[name_info['colors']](name_for_colors))], 
      'width': widths[(ord(x)-97) % len(widths)],
      'letter': x
    } for x in formatted_name[1]
  ]
  
  first_name_width = functools.reduce(lambda a, b: a + b, [x['width'] for x in first_name_as_stripes])
  second_name_width = functools.reduce(lambda a, b: a + b, [x['width'] for x in second_name_as_stripes])
  
  second_name_width_multiplier = (canvas_unit / 2) / second_name_width
  first_name_width_multiplier = (canvas_unit / 2) / first_name_width

  name_as_stripes_resized = [
    {
      'color': x['color'], 
      'letters': [x['letter']], 
      'width': x['width'] * first_name_width_multiplier,
      'is_end_of_name': False
    } for x in first_name_as_stripes
  ] + [
    {
      'color': x['color'],
      'letters': [x['letter']], 
      'width': x['width'] * second_name_width_multiplier,
      'is_end_of_name': False
    } for x in second_name_as_stripes
  ]

  finalised_stripes = name_as_stripes_resized + list(reversed(name_without_letters(name_as_stripes_resized))) + name_without_letters(name_as_stripes_resized)
  
  draw_square(get_combined_stripes(finalised_stripes))