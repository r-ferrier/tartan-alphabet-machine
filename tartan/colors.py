colors = {
  'hot_pink': [1, 0.34, 0.6],
  'yellow': [0.88,0.86,0.21],
  'purple': [0.84, 0.62, 1],
  'pale_blue': [0.6,0.75,0.87],
  'really_pale_blue': [0.83, 0.91, 0.98],
  'pale_pink': [0.96,0.69,0.86],
  'really_pale_pink': [0.98, 0.87, 0.94],
  'dark_blue': [0.41, 0.51, 1],
  'sunshine_yellow': [1, 0.91, 0.13],
  'light_green': [0.8, 0.88, 0.47],
  'dark_green': [0.4, 0.69, 0.43],
  'white': [1,1,1],
  'deep_orange': [1,0.59,0.42],
  'deep_green': [0.4, 0.5, 0.43],
  'muted_green': [0.62, 0.75, 0.48],
  'copper': [	0.89, 0.51, 0.31],
  }

park_colors = {
  'deep_green': [0.4, 0.5, 0.43],
  'muted_green': [0.62, 0.75, 0.48],
  'copper': [	0.89, 0.51, 0.31],
}

def family_colors_1(name):
  result = []
  
  middle_colors = [colors['yellow'], colors['sunshine_yellow'], colors['purple']]
  contrast_colors = [colors['white'], colors['really_pale_pink'], colors['really_pale_blue'], colors['dark_blue'], colors['dark_green'], colors['hot_pink'],]

  pale_colors_index = (ord(name[0])) % len(contrast_colors)
  result.append(contrast_colors.pop(pale_colors_index))
  # if one pale colour picked, remove the other one so two can't be picked
  if pale_colors_index < 3:
    contrast_colors.pop(0)
    contrast_colors.pop(0)

  middle_colors_index = (ord(name[2])) % len(middle_colors)
  result.append(middle_colors.pop(middle_colors_index))

  dark_colors_index = (ord(name[1])) % len(contrast_colors)
  result.append(contrast_colors.pop(dark_colors_index))
    
  return result

def family_colors_2(name):
  result = []
  
  family_colors = [colors['white'], colors['deep_orange'], colors['pale_blue'], colors['dark_green'], colors['yellow'], colors['purple'], colors['hot_pink'], colors['sunshine_yellow'], colors['pale_pink'], colors['dark_blue'], colors['light_green']] 
 
  for x in name[:3]:
    colors_index = (ord(x)) % len(family_colors)
    if (family_colors[colors_index]==colors['yellow']):
      result.append(family_colors.pop(colors_index))
      family_colors.remove(colors['light_green'])
    elif (family_colors[colors_index]==colors['light_green']):
      result.append(family_colors.pop(colors_index))
      family_colors.remove(colors['yellow'])
    elif (family_colors[colors_index]==colors['hot_pink']):
      result.append(family_colors.pop(colors_index))
      family_colors.remove(colors['deep_orange'])
    elif (family_colors[colors_index]==colors['deep_orange']):
      result.append(family_colors.pop(colors_index))
      family_colors.remove(colors['hot_pink'])
    else:
      result.append(family_colors.pop(colors_index)) 
    
  return result


def family_colors_3(name):
  result = []
  
  middle_colors = [colors['yellow'], colors['purple'], colors['sunshine_yellow'], colors['light_green'], colors['pale_blue']]
  contrast_colors = [colors['white'], colors['dark_green'], colors['really_pale_pink'], colors['pale_pink'], colors['dark_blue'], colors['sunshine_yellow'], colors['hot_pink']]

  pale_colors_index = (ord(name[0])) % len(contrast_colors)
  result.append(contrast_colors.pop(pale_colors_index))
  # if one pale colour picked, remove the other one so two can't be picked
  if pale_colors_index < 3:
    contrast_colors.pop(0)
    contrast_colors.pop(0)

  middle_colors_index = (ord(name[2])) % len(middle_colors)
  result.append(middle_colors.pop(middle_colors_index))

  dark_colors_index = (ord(name[1])) % len(contrast_colors)
  result.append(contrast_colors.pop(dark_colors_index))
    
  return result

def family_colors_5(name):
  result = []
  
  family_colors = [colors['deep_orange'], colors['hot_pink'], colors['really_pale_pink']] 
 
  for x in name[:3]:
    colors_index = (ord(x)) % len(family_colors)
    result.append(family_colors.pop(colors_index)) 
    
  return result

def family_colors_6(name):
  result = []
  
  # simple version
  family_colors = [colors['pale_blue'], colors['sunshine_yellow'], colors['pale_pink'],colors['dark_green'], colors['hot_pink'], colors['light_green']] 
 
  for x in name[:3]:
    colors_index = (ord(x)) % len(family_colors)
    result.append(family_colors.pop(colors_index)) 
    
  return result

def family_colors_7(name):
  result = []
  
  # simple version
  family_colors = [ park_colors['deep_green'], park_colors['muted_green'],park_colors['copper']] 
 
  for x in name[:3]:
    colors_index = (ord(x)) % len(family_colors)
    result.append(family_colors.pop(colors_index)) 
    
  return result

def outlined_colors(name):
  result = []
  family_colors = [ 'a', 'b', 'c'] 
 
  for x in name[:3]:
    colors_index = (ord(x)) % len(family_colors)
    result.append(family_colors.pop(colors_index))
    
  return result

def ensure_3_colors(name_for_colors):
  name = [outlined_colors(name_for_colors)[(ord(x)) % len(outlined_colors(name_for_colors))] for x in name_for_colors]

  if(len(list(set(name))) < 3 ):
    replace_char_at_index(name,name_for_colors,0)
  
  return name

def replace_char_at_index(name,name_for_colors,index):
  missing_color = '' 
  char_positions = []

  for x in [ 'a', 'b', 'c']:
    if (x not in list(set(name))):
      missing_color = x

  for i, x in enumerate(name_for_colors):
    if(x == name_for_colors[index]):
      char_positions.append(i)

  for x in char_positions:
    name[x] = missing_color
  
  if(len(list(set(name))) < 3 ):
    if(index == len(name)-1):
      return name
    else:
      print(name)
      replace_char_at_index(name,name_for_colors,index+1)

  return name