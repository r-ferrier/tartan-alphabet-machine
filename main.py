from drawBot import *
import sys, getopt
from tartan.helpers import to_snake_case
from tartan.tartan import draw_tartan
from tartan.outlined_tartan_A3 import draw_outlined_tartan_A3
from tartan.outlined_tartan_A4 import draw_outlined_tartan_A4
from tartan.outlined_tartan_A5 import draw_outlined_tartan_A5
import csv

#!/usr/bin/env python
def main():
  file_name = ""
  paper_size = 'A4'
  names = []

  argv = sys.argv[1:] 
  opts, args = getopt.getopt(argv,"hn:f:s:")

  for opt, arg in opts:
    if opt == '-h':
      print ('test.py -n <name> -f <filename> -s <size> \n-n <name> (optional): Person\'s name, in title case \n-f <filename> (optional): csv filename without extension, placed in the names folder\n-s <size> (required): size of paper - can be A4,A5 or A3')
      sys.exit()
    elif opt in ("-s"):
      paper_size = arg.upper()
    elif opt in ("-f"):
      file_name = arg
    elif opt in ("-n"):
      names = [arg]
    
  if len(names)>0:
    file_name = names[0]
    draw_outlined_tartan(names,paper_size,file_name)
  elif len(file_name)>0:
    with open(f'names/{file_name}.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      [names.append(row[0]) for row in csv_reader]
      draw_outlined_tartan(names,paper_size,file_name)
  else:
    print ('no names provided')
    sys.exit()
      

def draw_outlined_tartan(names,paper_size,file_name):
  db = drawBotDrawingTools.DrawBotDrawingTool()
  db.newDrawing()
  for (name) in names:
    draw_tartan_func = globals()[f'draw_outlined_tartan_{paper_size}']
    draw_tartan_func(db,name)
  db.endDrawing()
  path = f'./outputs/{to_snake_case(file_name)}_{paper_size}.pdf'
  db.saveImage(path)

# def draw_colourful_tartan():
    # name must be formatted as 'firstname familyname familyname' or 'firstname familyname'
    # names = []

    # with open('assets/outline-guests.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     for row in csv_reader:
    #         # names.append(({'name': row[1], 'initials': 'RF'}, f'family_colors_{row[0]}'))
    #         names.append(({'name': row[1], 'initials': row[2], 'colors': f'family_colors_{row[0]}','name_color': row[3]}))
           
    # db.newDrawing()

    # for (name_info) in names:
    #     draw_tartan(db,name_info)

    # db.endDrawing()
    # path = "./family-tartans.pdf"
    # db.saveImage(path)
    #
          
     
if __name__ == "__main__":
  main()

