from drawBot import *
from tartan.tartan_repeat import draw_tartan
import csv

#!/usr/bin/env python
def main():
    db = drawBotDrawingTools.DrawBotDrawingTool()
    db.newDrawing()

    # name must be formatted as 'firstname familyname familyname' or 'firstname familyname'
    names = []

    with open('assets/handfasting-tartan.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # names.append(({'name': row[1], 'initials': 'RF'}, f'family_colors_{row[0]}'))
            names.append(({'name': row[1], 'initials': row[2], 'colors': f'family_colors_{row[0]}','name_color': row[3]}))
    
    for (name_info) in names:
        draw_tartan(db,name_info)


    db.endDrawing()
    path = "./family-tartans.pdf"
    db.saveImage(path)           

if __name__ == "__main__":
    main()

