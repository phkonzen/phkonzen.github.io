#!/usr/bin/python3
'''
index.py

Autor: Pedro H A Konzen - 07/2022
Modificado: MM/YYYY
'''

import os

# output path
odir = './docs'

# head
head = '<head>'
head =  '<meta charset="utf-8">'
head += '<title>Notas de Aula</title>'
head += '<meta name="author" content="Pedro H A Konzen"/>\n'
head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'

#boostrap
head += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">'
head += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>'
head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>'

# FontAwesome
head += '<link href="./fontawesome/css/all.css" rel="stylesheet">'
head += '<link href="./fontawesome/css/brands.css" rel="stylesheet">'
head += '<link href="./fontawesome/css/solid.css" rel="stylesheet">'

# font Computer Modern Serif
head += '<link rel="stylesheet" href="fonts/cmun-serif.css"></link>'
head += '<link rel="stylesheet" href="index.css" type="text/css">'
        
head += '</head>'

# css
css = ''
# css += 'body {'
# css += 'font-family: "Computer Modern Serif", serif;'
# css += 'font-size: 100%;'
# css += '}'


# body
body = '<body>'

# card
body += '<div class="container mt-5" style="max-width: 400px;">'
body += '<div class="card border-primary" style="width: 18rem;">'
body += '<img class="jumbotrom" src="./pics/jumbotron2.jpg" alt="Páginas disponíveis">'
body += '<div class="card-body">'
body += '<h5 class="card-title">Acessar</h5>'

body += '<div class="list-group">'
body += '<a href="https://phkonzen.github.io/notas" class="list-group-item list-group-item-action border-warning">'
body += '<i class="fa-solid fa-file-lines" style="color: blue;"></i> Notas de Aula</a>'
body += '<a href="https://www.instagram.com/notas.pedrok/" class="list-group-item list-group-item-action"><i class="fab fa-instagram" style="color: blue;"></i> Perfil Instagram</a>'
body += '<a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA" class="list-group-item list-group-item-action"><i class="fab fa-youtube" style="color: red;"></i> Canal Youtube</a>'
body += '<a href="https://archive.org/details/notas-de-aula" class="list-group-item list-group-item-action"><i class="fas fa-building-columns" style="color: blue;"></i> Coleção archive.org</a>'
body += '<a href="https://github.com/phkonzen/notas" class="list-group-item list-group-item-action"><i class="fab fa-github" style="color: blue;"></i> Repositório GitHub</a>'
body += '<a href="https://professor.ufrgs.br/pedro" class="list-group-item list-group-item-action">'
body += '<img class="favicon" src="./pics/favicon.ico"></img> Página Professor UFRGS</a>'
body += '</div>'

body += '</div>'
body += '</div>'
body += '</div>'


body += '</body>'

# build page
pname = 'index'

html = '<html lang="pt">'
html += head
html += body
html += '</hmtl>'

f = open(odir + '/' + pname + '.html', 'w')
f.write(html)
f.close()

f = open(odir + '/' + pname + '.css', 'w')
f.write(css)
f.close()

#fonts
os.system('cp -rvf ./fonts ' + odir + '/')

#fontawesome
os.system('cp -rvf ./fontawesome ' + odir + '/')

#pics
os.system('cp -rvf ./pics ' + odir + '/')
