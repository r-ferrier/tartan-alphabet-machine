import functools 
from drawBot import *
from tartan.colors import outlined_colors
from tartan.tartan_info.letters_key_A5 import draw_letters_key
from tartan.constants import canvas_width_A5, canvas_height_A5, margin_A5, y_tartan_offset_A5, label_gap_A5, fontSize_A5
from tartan.helpers import name_without_spaces, get_unique_colors
from unidecode import unidecode

def draw_outlined_tartan_A5(drawbot: drawBotDrawingTools.DrawBotDrawingTool, name):

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
  
  def draw_key_lines(x1,x2,y1,y2,color,colors):
    x_margin_80_pct = (margin_A5 - (label_gap_A5*2))
    x_margin_70_pct = (margin_A5 - (label_gap_A5*3))
    x_margin_60_pct = (margin_A5 - (label_gap_A5*4))
    
    y_margin_80_pct = (margin_A5 - (label_gap_A5*2)) + y_tartan_offset_A5
    y_margin_70_pct = (margin_A5 - (label_gap_A5*3)) + y_tartan_offset_A5
    y_margin_60_pct = (margin_A5 - (label_gap_A5*4)) + y_tartan_offset_A5

    drawbot.line((x1, y_margin_80_pct),(x2,y_margin_80_pct))
    drawbot.line((x_margin_80_pct, y1),(x_margin_80_pct, y2))

    if(len(colors) > 1 and color == colors[1]):
      drawbot.line((x1, y_margin_70_pct),(x2,y_margin_70_pct))
      drawbot.line((x_margin_70_pct, y1),(x_margin_70_pct, y2))
    
    if (len(colors) > 2 and color == colors[0]):
      drawbot.line((x1, y_margin_70_pct),(x2,y_margin_70_pct))
      drawbot.line((x_margin_70_pct, y1),(x_margin_70_pct, y2))
      drawbot.line((x1, y_margin_60_pct),(x2,y_margin_60_pct))
      drawbot.line((x_margin_60_pct, y1),(x_margin_60_pct, y2))

  def get_name_widths(name,drawbot):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_widths = { x: drawbot.textSize(x)[0] for x in letters }
    return [letter_widths[x] for x in unidecode(name)]
  
  def draw_square(stripes):
    drawbot.stroke(0,0,0)
    drawbot.fill(1,1,1,0)
    # drawbot.rect(margin, margin, canvas_width, canvas_width)

    for index, character in enumerate(stripes):
      width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
      width = character['width']

      x1 = margin_A5 + (width_so_far - width)
      y1 = margin_A5 + y_tartan_offset_A5
      
      x2 = margin_A5
      y2 = margin_A5 + (width_so_far - width) + y_tartan_offset_A5

      drawbot.rect(x1,y1,width,canvas_width_A5)
      drawbot.rect(x2,y2,canvas_width_A5,width)

      draw_key_lines(
        x1 + (label_gap_A5 / 2),
        (x2 + width_so_far)-(label_gap_A5/2),
        (y1 + width_so_far)-(label_gap_A5/2),
        y2 + (label_gap_A5 / 2),
        character['color'],
        get_unique_colors([x['color'] for x in stripes])
      )
      
  def draw_name(name):
    drawbot.strokeWidth(0)
    drawbot.fill(0,0,0,1)
    drawbot.text(name,(margin_A5,y_tartan_offset_A5))
    drawbot.strokeWidth(1)


  drawbot.newPage(canvas_width_A5 + margin_A5 * 2, canvas_height_A5 + margin_A5 * 2)
  fontName = drawbot.installFont('./assets/CormorantGaramond-Light.ttf')
  drawbot.font(fontName, fontSize_A5)
  drawbot.strokeWidth(1)

  name_for_colors = name.lower().split(" ")[-1]
  name_for_tartan = name_without_spaces(name.lower())
  name_widths = get_name_widths(name_without_spaces(name.lower()), drawbot)
  name_width = functools.reduce(lambda a, b: a + b, name_widths)

  name_as_stripes = [
    {
      'color': outlined_colors(name_for_colors)[(ord(x)-97) % len(outlined_colors(name_for_colors))], 
      'width': name_widths[index] * ((canvas_width_A5) / name_width),
      'letters': [x],
      'is_end_of_name': False
    } for index, x in enumerate(name_for_tartan)
  ]
  
  draw_square(get_combined_stripes(name_as_stripes))
  draw_name(name)
  draw_letters_key(drawbot,name_as_stripes,((canvas_width_A5 / 3) / name_width),name)