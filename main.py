from drawBot import *
from tartan.tartan import draw_tartan
from tartan.outlined_tartan import draw_outlined_tartan
import csv

#!/usr/bin/env python
def main():
    # name must be formatted as 'firstname familyname familyname' or 'firstname familyname'
    names = []
    with open('assets/guests.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # names.append(({'name': row[1], 'initials': 'RF'}, f'family_colors_{row[0]}'))
            names.append(({'name': row[1], 'initials': row[2], 'colors': f'family_colors_{row[0]}','name_color': row[3]}))
    
    db = drawBotDrawingTools.DrawBotDrawingTool()
    
    db.newDrawing()

    for (name_info) in names:
        draw_tartan(db,name_info)

    db.endDrawing()
    path = "./family-tartans.pdf"
    db.saveImage(path)      

    db.newDrawing()

    for (name_info) in names:
            draw_outlined_tartan(db,name_info)

    db.endDrawing()
    path = "./outlined-tartans.pdf"
    db.saveImage(path)     
     

if __name__ == "__main__":
    main()

