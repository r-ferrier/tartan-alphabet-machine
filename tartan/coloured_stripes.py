import functools 
from drawBot import *

def draw_coloured_stripes(drawbot: drawBotDrawingTools.DrawBotDrawingTool, stripes, colors, args):
  drawbot.stroke(0,0,0,0)
  drawbot.blendMode("multiply")

  for index, character in enumerate(stripes):
    drawbot.fill(*colors[character['color']])

    width_so_far = functools.reduce(lambda a, b: a + b, [x['width'] for x in stripes[0:index+1]])      
    width = character['width']

    x1 = args["margin"] + (width_so_far - width)
    y1 = args["margin"] + args["y_tartan_offset"]
    
    x2 = args["margin"]
    y2 = args["margin"] + (width_so_far - width) + args["y_tartan_offset"]

    drawbot.rect(x1,y1,width,args["canvas_width"])
    drawbot.rect(x2,y2,args["canvas_width"],width)