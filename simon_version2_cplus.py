from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_Joystick3 = hat.get(hat.JOYSTICK)

atrouver = None
niveau = None
fdj = None
dir2 = None
sequence = None
high_score = None
action = None
i = None
k = None
continue2 = None
x = None
y = None


niveau_en_cours = M5TextBox(100, 219, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label0 = M5TextBox(42, 97, "Suite dans", lcd.FONT_Default, 0xFFFFFF, rotate=0)
nivea = M5TextBox(10, 218, "Niveau", lcd.FONT_Default, 0xFFFFFF, rotate=0)
action_a_effectuer = M5TextBox(19, 72, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
rebours = M5TextBox(42, 119, "Text", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label4 = M5TextBox(41, 149, "Text", lcd.FONT_DejaVu72, 0xFFFFFF, rotate=0)
sens = M5TextBox(45, 47, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)

import random
from numbers import Number


def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)



dir2 = ['^', 'v', '<', '>']
sequence = []
high_score = 0
niveau = 1
action = '-'
i = 0
k = 3
continue2 = 1
setScreenColor(0x000000)
niveau_en_cours.setText('')
label0.setColor(0x000000)
nivea.setColor(0x000000)
sens.setColor(0x000000)
while True:
  M5Led.off()
  niveau = 1
  nivea.setColor(0x000000)
  niveau_en_cours.setColor(0x000000)
  while btnA.isReleased():
    action_a_effectuer.setText('Appuyez sur A')
    action = '-'
    atrouver = random.randint(1, 4)
  niveau_en_cours.setColor(0xffffff)
  sequence = []
  fdj = 0
  while fdj != 1:
    label4.setText('')
    label0.setColor(0xff0000)
    action_a_effectuer.setColor(0x000000)
    rebours.setColor(0x990000)
    k = 3
    nivea.setColor(0xffffff)
    niveau_en_cours.setText(str(niveau))
    for count in range(3):
      rebours.setText(str(k))
      wait(0.5)
      k = (k if isinstance(k, Number) else 0) + -1
    label0.setColor(0x000000)
    rebours.setColor(0x000000)
    niveau_en_cours.setText(str(niveau))
    M5Led.off()
    label4.setText('')
    atrouver = dir2[int(random.randint(1, 4) - 1)]
    sequence.append(atrouver)
    for i in (1 <= float(niveau)) and upRange(1, float(niveau), 1) or downRange(1, float(niveau), 1):
      M5Led.off()
      label4.setText(' ')
      wait(0.2)
      atrouver = sequence[int(i - 1)]
      if atrouver == '^':
        label4.setColor(0xff0000)
      if atrouver == 'v':
        label4.setColor(0xffff00)
      if atrouver == '<':
        label4.setColor(0x009900)
      if atrouver == '>':
        label4.setColor(0x33ccff)
      label4.setText(str(sequence[int(i - 1)]))
      M5Led.on()
      wait(1)
    action_a_effectuer.setColor(0xffffff)
    action_a_effectuer.setText('repetez la             sequence')
    label4.setText('')
    for i in (1 <= float(niveau)) and upRange(1, float(niveau), 1) or downRange(1, float(niveau), 1):
      continue2 = 1
      action = '-'
      label4.setColor(0x000000)
      while fdj == 0 and continue2 == 1:
        M5Led.off()
        x = hat_Joystick3.X
        y = hat_Joystick3.Y
        if y > 80:
          action = '^'
          label4.setColor(0xff0000)
          M5Led.on()
        if y < -20:
          action = 'v'
          label4.setColor(0xffff00)
          M5Led.on()
        if x < -20:
          action = '<'
          label4.setColor(0x009900)
          M5Led.on()
        if x > 80:
          action = '>'
          label4.setColor(0x33ccff)
          M5Led.on()
        sens.setText(str(sequence[int(i - 1)]))
        wait(0.5)
        label4.setText(str(action))
        if action == sequence[int(i - 1)]:
          action_a_effectuer.setText('ok')
          wait(0.5)
          continue2 = 0
          action_a_effectuer.setText('suite')
        else:
          if action != '-':
            action = '#'
            i = (i if isinstance(i, Number) else 0) + 1
            continue2 = 0
            action_a_effectuer.setText('ko')
            wait(0.5)
            action_a_effectuer.setText('fin du jeu')
            wait(1)
            fdj = 1
        label4.setText('')
      continue2 = 1
    if fdj == 1:
      action_a_effectuer.setColor(0x000000)
    else:
      action_a_effectuer.setColor(0xffffff)
    action_a_effectuer.setText('niveau suivant')
    niveau = (niveau if isinstance(niveau, Number) else 0) + 1
    wait(1)
    action_a_effectuer.setColor(0xffffff)
  wait_ms(2)
