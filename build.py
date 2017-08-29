#!/usr/bin/env python
import jinja2
import os

directory_name = './gifs/'
width = 32
height = 32

files = sorted(os.listdir(directory_name))

templateLoader = jinja2.FileSystemLoader( searchpath='./templates' )
templateEnv = jinja2.Environment( loader=templateLoader )

TEMPLATE_FILE = 'index.jinja'
template = templateEnv.get_template( TEMPLATE_FILE )


letters = []
for char in '0123456789abcdefghijklmnopqrstuvwxyz':
    emojis = []
    for file in files:
        if file[0] == char:
            basename = os.path.splitext(file)[0]
            emojis.append({'directory_name': directory_name,
                           'file': file,
                           'width': width,
                           'height': height,
                           'basename': basename})
    if len(emojis) > 0:
        letters.append({'char': char, 'emojis': emojis})

templateVars = { 'letters': letters }

output_text = template.render(templateVars)

with open("index.html", "w") as text_file:
        text_file.write(''.join(output_text))
