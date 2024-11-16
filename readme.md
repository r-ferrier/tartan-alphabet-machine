This code generates a DIY tartan pattern based on a string input.
You can read more about this project here: https://www.half-year-studio.com/diy-tartan
## How to run

Activate virtual environment:
`source tartan_env/bin/activate`

Run:
`python3 main.py -n <name> -f <filename> -s <size> -c <complexity>  -b <background>`

-n (optional): Person's name, in title case
-f (optional): csv filename without extension, placed in the names folder
-s (defaults to A4): size of paper - can be A4, A5 or A3
-c (defaults to 1): complexity - can be 1, 2, or 3 pattern repeats
-b (defaults to false): background color - if included adds colour

Stop virtual environment:
`deactivate`

Getting drawbot working is really hard! I don't know why!
Reinstall it with: `pip3 install git+https://github.com/typemytype/drawbot`
