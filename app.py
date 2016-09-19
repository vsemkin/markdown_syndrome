#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from flask import *
app = Flask(__name__)

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route('/', methods=['GET'])
def all1_users():
    return render_template('index.html', s="")
    
## use the s variable to print

@app.route('/', methods=['POST'])
def all_users():
    md = request.form['md']
    lines = md.splitlines()
    s = ""
    for i in range(len(lines)):
        if (lines[i] == ''):
            break
        
        counter = 0
        for j in range(len(lines[i])):
            if (lines[i][j] == '*'):
                counter += 1
        
        nopar = False
        if (counter == 1):
            lines[i] = lines[i].replace('*','<li>', 1)
            s +=lines[i] + '</li>' + '\n'
            nopar = True
        
        
        ## bold
        while (lines[i].find('__') != -1) or (lines[i].find('**') != -1):
            lines[i] = lines[i].replace('__', '<b>', 1)   
            lines[i] = lines[i].replace('__', '</b>', 1)     
            lines[i] = lines[i].replace('**', '<b>', 1)   
            lines[i] = lines[i].replace('**', '</b>', 1)   
        
        ## italics
        while (lines[i].find('_') != -1) or (lines[i].find('*') != -1):
            lines[i] = lines[i].replace('_', '<i>', 1)   
            lines[i] = lines[i].replace('_', '</i>', 1)     
            lines[i] = lines[i].replace('*', '<i>', 1)   
            lines[i] = lines[i].replace('*', '</i>', 1)
        
        ## strikethrough
        while (lines[i].find('~~') != -1):
            lines[i] = lines[i].replace('~~', '<strike>', 1)   
            lines[i] = lines[i].replace('~~', '</strike>', 1)   
            
        ##code
        while (lines[i].find('```') != -1):
            lines[i] = lines[i].replace('```', '<code>', 1)   
            lines[i] = lines[i].replace('```', '</code>', 1)  
        while (lines[i].find('``') != -1):
            lines[i] = lines[i].replace('``', '<code>', 1)   
            lines[i] = lines[i].replace('``', '</code>', 1) 
        while (lines[i].find('`') != -1):
            lines[i] = lines[i].replace('`', '<code>', 1)   
            lines[i] = lines[i].replace('`', '</code>', 1)    
        
            
        ## headings
        if (lines[i][0] == '#') and (lines[i][1] == '#') and (lines[i][2] == '#') and (lines[i][3] == '#') and (lines[i][4] == '#') and (lines[i][5] == '#'):
            s += '<h6>'+lines[i][6:]+'</h6>' + '\n'
        elif (lines[i][0] == '#') and (lines[i][1] == '#') and (lines[i][2] == '#') and (lines[i][3] == '#') and (lines[i][4] == '#'):
            s += '<h5>'+lines[i][5:]+'</h5>' + '\n'
        elif (lines[i][0] == '#') and (lines[i][1] == '#') and (lines[i][2] == '#') and (lines[i][3] == '#'):
            s += '<h4>'+lines[i][4:]+'</h4>' + '\n'
        elif (lines[i][0] == '#') and (lines[i][1] == '#') and (lines[i][2] == '#'):
            s += '<h3>'+lines[i][3:]+'</h3>' + '\n'
        elif (lines[i][0] == '#') and (lines[i][1] == '#'):
            s += '<h2>'+lines[i][2:]+'</h2>' + '\n'
        elif (lines[i][0] == '#'):
            s += '<h1>'+lines[i][1:]+'</h1>' + '\n'
        ##blockquates
        elif (lines[i][0] == '>'):
            s += '<blockquote>'+lines[i][1:]+'</blockquote>'+'\n'
        ##unordered lists
        elif (lines[i][0] == '+'):
            s += '<li>'+lines[i][1:]+'</li>'+'\n'
        elif (lines[i][0] == '-'):
            s += '<li>'+lines[i][1:]+'</li>'+'\n'
        elif (nopar == False):
            s += '<p>'+lines[i]+'</p>' + '\n'
            
    return render_template('index.html', s=s, md=md, z=s)      

    
if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host='0.0.0.0')
