from tartan.constants import first_lines_max_width
import re
import string

def name_without_punctuation(name):
  return name.translate(str.maketrans('', '', string.punctuation))

def get_unique_colors(colors):
    new_colors = []
    for color in colors:
      if color not in new_colors:
        new_colors.append(color)
    return new_colors

def normalize_width(width, largest_width):
  return float(width) * (first_lines_max_width / largest_width)

def to_snake_case(string):
  return re.sub(r'(?<=[a-z])(?=[A-Z])|[^a-zA-Z]', '_', string).strip('_').lower()
