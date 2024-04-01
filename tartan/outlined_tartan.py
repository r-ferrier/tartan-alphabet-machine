import functools 
from drawBot import *
from tartan.colors import ensure_3_colors, outlined_colors
from tartan.tartan_info.letters_key import draw_letters_key
from tartan.coloured_stripes import draw_coloured_stripes
from tartan.helpers import name_without_punctuation, get_unique_colors
from tartan.colors import abc_colors

def draw_outlined_tartan(drawbot: drawBotDrawingTools.DrawBotDrawingTool, name, complexity, args):
  
  # helpers ----------------------------------------------
  
  def get_names_for_square(complexity,name_as_stripes):
    names_for_square = []
    match complexity:
      case 1:
        names_for_square = name_as_stripes
      case 2:
        names_for_square = name_as_stripes + list(reversed(name_as_stripes)) 
      case 3:
        names_for_square = name_as_stripes + list(reversed(name_as_stripes)) + name_as_stripes
      case _:
        names_for_square = name_as_stripes
    return get_combined_stripes(names_for_square)

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
    x_margin_80_pct = (args["margin"] - (args["label_gap"]*2))
    x_margin_70_pct = (args["margin"] - (args["label_gap"]*3))
    x_margin_60_pct = (args["margin"] - (args["label_gap"]*4))
    
    y_margin_80_pct = (args["margin"] - (args["label_gap"]*2)) + args["y_tartan_offset"]
    y_margin_70_pct = (args["margin"] - (args["label_gap"]*3)) + args["y_tartan_offset"]
    y_margin_60_pct = (args["margin"] - (args["label_gap"]*4)) + args["y_tartan_offset"]

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

  def get_name_widths(name):
    name_as_array = []
    for char in name:
        if char not in name_as_array:
            name_as_array.append(char)
    letter_widths = { x: drawbot.textSize(x)[0] for x in name_as_array }
    return [letter_widths[x] for x in name]

  def draw_square(stripes):
    drawbot.stroke(0,0,0)
    drawbot.fill(1,1,1,0)
    # drawbot.rect(margin, margin, canvas_width, canvas_width)

    for index, character in enumerate(stripes):
      width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
      width = character['width']

      x1 = args["margin"] + (width_so_far - width)
      y1 = args["margin"] + args["y_tartan_offset"]
      
      x2 = args["margin"]
      y2 = args["margin"] + (width_so_far - width) + args["y_tartan_offset"]

      drawbot.rect(x1,y1,width,args["canvas_width"])
      drawbot.rect(x2,y2,args["canvas_width"],width)

      draw_key_lines(
        x1 + (args["label_gap"] / 2),
        (x2 + width_so_far)-(args["label_gap"]/2),
        (y1 + width_so_far)-(args["label_gap"]/2),
        y2 + (args["label_gap"] / 2),
        character['color'],
        get_unique_colors([x['color'] for x in stripes])
      )
      
  def draw_name(name):
    drawbot.strokeWidth(0)
    drawbot.fill(0,0,0,1)
    drawbot.text(name,(args["margin"],(args["y_tartan_offset"] - args["title_offset"])))
    drawbot.strokeWidth(1)

  # main body of method ----------------------------------------------
  
  drawbot.newPage(args["canvas_width"] + args["margin"] * 2, args["canvas_height"] + args["margin"] * 2)
  fontName = drawbot.installFont('./assets/CormorantGaramond-Light.ttf')
  drawbot.font(fontName, args["font_size"])
  drawbot.strokeWidth(1)

  name_for_tartan = name_without_punctuation(name.lower())
  name_widths = get_name_widths(name_without_punctuation(name.lower()))
  name_width = functools.reduce(lambda a, b: a + b, name_widths)
  name_with_3_colors = ensure_3_colors(name_for_tartan)

  name_as_stripes = [
    {
      'color': name_with_3_colors[index],
      'width': name_widths[index] * ((args["canvas_width"] / complexity) / name_width),
      'letters': [x],
      'is_end_of_name': False
    } for index, x in enumerate(name_for_tartan)
  ]


  names_for_square = get_names_for_square(complexity,name_as_stripes)
  name_colors = abc_colors(name.lower())

  draw_square(names_for_square)
  draw_name(name)
  draw_letters_key(drawbot, name_as_stripes, name_for_tartan, name_colors, args)
  if(args["with_colour"]):
    draw_coloured_stripes(drawbot,names_for_square,name_colors,args)