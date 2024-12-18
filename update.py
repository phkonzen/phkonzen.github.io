import sys
import os

import linktree

odir = './docs'

def update_linktree():
  linktree.deploy(odir)

def update_notas():
  os.system('rsync -av --delete ../notas/docs/ ' + odir + '/notas/')

# do it
option = 'all'
if (len(sys.argv) > 1):
  option = sys.argv[1]

if (option == 'linktree'):
  update_linktree()
elif (option == 'notas'):
  update_notas()
elif (option == 'all'):
  update_linktree()
  update_notas()
else:
  raise Exception('Usage: update.py [linktree | notas | all]')