from drawBot import *
from tartan.tartan_full_size import draw_tartan
import csv

canvas_unit = 1000

#!/usr/bin/env python
def main():
    db = drawBotDrawingTools.DrawBotDrawingTool()
    db.newDrawing()

    # name must be formatted as 'firstname familyname familyname' or 'firstname familyname'
    names = []

    with open('assets/guests.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            names.append(({'name': row[1], 'initials': row[2], 'colors': f'family_colors_{row[0]}','name_color': row[3]}))


    width_multiplier = 3
    height_multiplier = 4
    x_offset = 0
    y_offset = 0


    db.newPage(width_multiplier * (3 * canvas_unit), (height_multiplier * (3 * canvas_unit)))
    
    for (name_info) in names:
        draw_tartan(db,name_info,x_offset*(canvas_unit*3),y_offset*(canvas_unit*3))
        if(x_offset < 2):
            x_offset += 1
        else:
            x_offset = 0
            if(y_offset < 3):
                y_offset += 1
            else:
                y_offset = 0
                db.newPage(width_multiplier * (3 * canvas_unit), (height_multiplier * (3 * canvas_unit)))


    db.endDrawing()
    path = "./family-tartans.pdf"
    db.saveImage(path)           

if __name__ == "__main__":
    main()

