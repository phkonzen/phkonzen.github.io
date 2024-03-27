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
head += '<title>NotasPedroK</title>'
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
        
#google tracking
f = open('gtag.js','r')
head += f.read()
f.close()

head += '</head>'

# css
css = ''
css += '.title {'
css += 'font-family: "Computer Modern Serif", serif;'
css += '}'
css += '.mybtn {'
css += 'width: 20rem !important;'
css += '}'


# body
body = '<body>'

# general alert
f = open('general_alert.html','r')
body += f.read()
f.close()

body += '<div class="container-fluid d-flex justify-content-center mt-2 mb-2">'

body += '<a href="https://www.notaspedrok.com.br/notas"><img src="./pics/logoPenguin.png" class="rounded-circle mx-auto d-block" alt="Notas de Aula" style="width: 15rem; height: auto;"></a>'
body += '</div>'

body += '<div class="container-fluid justify-content-center mb-2">'
body += '<h2 class="d-flex justify-content-center mb-0 title">'
body += 'NotasPedroK'
body += '</h2>'
body += '<p class="d-flex justify-content-center mt-0 title">Pedro H A Konzen</p></p>'
body += '</div>'

body += '<p class="d-flex justify-content-center"><a class="btn btn-primary mybtn" href="https://phkonzen.github.io/notas" role="button"><i class="fa-solid fa-file-lines"></i> &nbsp Site Oficial</a></p>'

body += '<p class="d-flex justify-content-center"><a href="https://professor.ufrgs.br/pedro" class="btn btn-primary mybtn"><img src="./pics/favicon.ico"></img> &nbsp Site de Professor na UFRGS</a></p>'

body += '<p class="d-flex justify-content-center"><a href="https://www.instagram.com/notas.pedrok/" class="btn btn-primary mybtn"><i class="fab fa-instagram"></i> &nbsp @notas.pedrok</a></p>'

body += '<p class="d-flex justify-content-center"><a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA" class="btn btn-primary mybtn"><i class="fab fa-youtube"></i> &nbsp Canal do Youtube</a></p>'

body += '<p class="d-flex justify-content-center"><a href="https://archive.org/details/notas-de-aula" class="btn btn-primary mybtn"><i class="fas fa-building-columns""></i> &nbsp Coleção no archive.org</a></p>'

body += '<p class="d-flex justify-content-center"><a href="https://github.com/phkonzen/notas" class="btn btn-primary mybtn"><i class="fab fa-github"></i> &nbsp Repositório GitHub</a></p>'
1
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
