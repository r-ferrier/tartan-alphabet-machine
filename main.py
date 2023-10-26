from drawBot import *
import sys, getopt
from tartan.helpers import to_snake_case
from tartan.tartan import draw_tartan
from tartan.constants import outlined_args
from tartan.outlined_tartan import draw_outlined_tartan
import csv

#!/usr/bin/env python
def main():
  file_name = ""
  paper_size = 'A4'
  names = []
  complexity = 1

  argv = sys.argv[1:] 
  opts, args = getopt.getopt(argv,"hn:f:s:c:")

  for opt, arg in opts:
    if opt == '-h':
      print ('test.py -n <name> -f <filename> -s <size> -c <complexity>')
      sys.exit()
    elif opt in ("-s"):
      paper_size = arg.upper()
    elif opt in ("-f"):
      file_name = arg
    elif opt in ("-n"):
      names = [arg]
    elif opt in ("-c"):
      complexity = int(arg)

  if len(list(set(names[0]))) < 3:
    print('\x1b[0;33;40m'+f'Not enough unique characters to create a tartan for this name'+'\x1b[0m')
    sys.exit()
  
  print('\x1b[0;32;40m'+f'Creating tartan for {names} \nSize: {paper_size}\nPattern repeats: {complexity}'+'\x1b[0m')

  if len(names)>0:
    file_name = names[0]
    make_outlined_drawing(names,paper_size,complexity,file_name)
  elif len(file_name)>0:
    with open(f'names/{file_name}.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      [names.append(row[0]) for row in csv_reader]
      make_outlined_drawing(names,paper_size,complexity,file_name)
  else:
    print ('no names provided')
    sys.exit()
      

def make_outlined_drawing(names,paper_size,complexity,file_name):
  db = drawBotDrawingTools.DrawBotDrawingTool()
  db.newDrawing()
  for (name) in names:
    draw_outlined_tartan(db,name,complexity,outlined_args[paper_size])
  db.endDrawing()
  path = f'./outputs/{to_snake_case(file_name)}_{paper_size}.pdf'
  db.saveImage(path)
  print('\x1b[0;35;40m'+f'File saved to: {path}'+'\x1b[0m')

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

