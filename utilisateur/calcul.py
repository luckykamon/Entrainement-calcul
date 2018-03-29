import time
import sys
from random import randint
import pygame
from pygame.locals import *


pygame.init()
window = pygame.display.set_mode((648, 604), RESIZABLE)


def initialisation(): #choice beetween play or help
  window.blit(pygame.image.load("start.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 489 > event.pos[1]:
            choice(0)
          if 488 < event.pos[1]:
            help()
      if event.type == KEYDOWN:
        choice(0)

def help(): #display help
  window.blit(pygame.image.load("help.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        initialisation()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          initialisation()

def menu(a): #choice beetween replay or go start
  window.blit(pygame.image.load("menu.png").convert(), (230, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 200 < event.pos[1] < 239:
            if 230 < event.pos[0] < 364:
              initialisation()
            if 364 < event.pos[0] < 498:
              choice(a)
      if event.type == KEYDOWN:
        if event.key == K_KP0:
          initialisation()
        if event.key == K_KP1:
          choice(a)

def choice(a):#choice beetween add sous and mul
  if a==1:
    add()
  if a==2:
    sous()
  if a==3:
    mul()
  window.blit(pygame.image.load("choice.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if event.pos[1] < 202:
            add()
          if 201 < event.pos[1] < 404:
            sous()
          if 403 < event.pos[1]:
            mul()

def add():
  window.blit(pygame.image.load("white.png").convert(), (0, 0))
  pygame.display.flip()
  j=0
  r=0
  a,b,c,d,e=0,0,0,0,0
  a=randint(1000,10000)
  b=randint(1000,10000)
  c=randint(1000,10000)
  d=randint(1000,10000)
  e=randint(1000,10000)
  window.blit(pygame.font.Font(None, 150).render("   "+str(a),1,(0,0,0)), (160,20))
  window.blit(pygame.font.Font(None, 150).render("+ "+str(b),1,(0,0,0)), (160,120))
  window.blit(pygame.font.Font(None, 150).render("+ "+str(c),1,(0,0,0)), (160,220))
  window.blit(pygame.font.Font(None, 150).render("+ "+str(d),1,(0,0,0)), (160,320))
  window.blit(pygame.font.Font(None, 150).render("+ "+str(e),1,(0,0,0)), (160,420))
  window.blit(pygame.font.Font(None, 150).render("______",1,(0,0,0)), (160,420))
  pygame.display.flip()
  j=a+b+c+d+e
  result = []
  n = 0 #number of letter
  ch = 0 #select letter
  while True:
    ch = touche(0)
    if ch == -1:
      break
    if ch == -2 and n > 0:
      del result[0]
      n -= 1
    if ch != -2 and n < 5:
      result=[ch]+result
      n += 1
    window.blit(pygame.image.load("white.png").convert(), (0, 522))
    for i in range(len(result)):
      window.blit(pygame.font.Font(None, 150).render(str(result[-i-1]),1,(0,0,0)), (440-i*60,522))
    pygame.display.flip()
  while len(result) <5:
    result=[0]+result
  finish = 0
  for k in range(len(result)):
    finish+=result[-k-1]*10**(k)
  if finish==j:
    window.blit(pygame.image.load("white.png").convert(), (0, 522))
    window.blit(pygame.font.Font(None, 150).render(str(j),1,(0,255,0)), (200,522))
  else:
    window.blit(pygame.image.load("white.png").convert(), (0, 522))
    window.blit(pygame.font.Font(None, 150).render(str(j),1,(255,0,0)), (200,522))
  pygame.display.flip()
  menu(1)

def sous():
  window.blit(pygame.image.load("white.png").convert(), (0, 0))
  pygame.display.flip()
  j=0
  r=0
  a,b,c=0,0,0
  a=randint(2000,10000)
  b=randint(100,1000)
  c=randint(100,1000)
  window.blit(pygame.font.Font(None, 150).render("   "+str(a),1,(0,0,0)), (175,20))
  window.blit(pygame.font.Font(None, 150).render("- "+str(b),1,(0,0,0)), (250,120))
  window.blit(pygame.font.Font(None, 150).render("- "+str(c),1,(0,0,0)), (250,220))
  window.blit(pygame.font.Font(None, 150).render("______",1,(0,0,0)), (160,220))
  pygame.display.flip()
  j=a-b-c
  result = []
  n = 0 #number of letter
  ch = 0 #select letter
  while True:
    ch = touche(0)
    if ch == -1:
      break
    if ch == -2 and n > 0:
      del result[0]
      n -= 1
      window.blit(pygame.image.load("white.png").convert(), (0, 322))
    if ch != -2 and n < 4:
      result=[ch]+result
      n += 1
    window.blit(pygame.image.load("white.png").convert(), (0, 522))
    for i in range(len(result)):
      window.blit(pygame.font.Font(None, 150).render(str(result[-i-1]),1,(0,0,0)), (440-i*60,322))
    pygame.display.flip()
  while len(result) <5:
    result=[0]+result
  finish = 0
  for k in range(len(result)):
    finish+=result[-k-1]*10**(k)
  if finish==j:
    window.blit(pygame.image.load("white.png").convert(), (0, 322))
    window.blit(pygame.font.Font(None, 150).render(str(j),1,(0,255,0)), (250,322))
  else:
    window.blit(pygame.image.load("white.png").convert(), (0, 322))
    window.blit(pygame.font.Font(None, 150).render(str(j),1,(255,0,0)), (250,322))
  pygame.display.flip()
  menu(2)

def mul():
  window.blit(pygame.image.load("white.png").convert(), (0, 0))
  pygame.display.flip()
  j=0
  r=0
  a,b=0,0
  a=randint(100,1000)
  b=randint(100,1000)
  window.blit(pygame.font.Font(None, 150).render("   "+str(a),1,(0,0,0)), (240,20))
  window.blit(pygame.font.Font(None, 150).render("X   "+str(b),1,(0,0,0)), (160,120))
  window.blit(pygame.font.Font(None, 150).render("______",1,(0,0,0)), (160,120))
  pygame.display.flip()
  j=a*b
  result = []
  n = 0 #number of letter
  ch = 0 #select letter
  while True:
    ch = touche(0)
    if ch == -1:
      break
    if ch == -2 and n > 0:
      del result[0]
      n -= 1
    if ch != -2 and n < 6:
      result=[ch]+result
      n += 1
    window.blit(pygame.image.load("white.png").convert(), (0, 222))
    for i in range(len(result)):
      window.blit(pygame.font.Font(None, 150).render(str(result[-i-1]),1,(0,0,0)), (440-i*60,222))
    pygame.display.flip()
  while len(result) <5:
    result=[0]+result
  finish = 0
  for k in range(len(result)):
    finish+=result[-k-1]*10**(k)
  if finish==j:
    window.blit(pygame.image.load("white.png").convert(), (0, 222))
    window.blit(pygame.font.Font(None, 150).render(str(j),1,(0,255,0)), (140,222))
  else:
    window.blit(pygame.image.load("white.png").convert(), (0, 222))
    window.blit(pygame.font.Font(None, 150).render(str(j),1,(255,0,0)), (140,222))
  pygame.display.flip()
  menu(3)

def touche(a):
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        if a == 0:
          if event.key == K_RETURN:
            return -1
          if event.key == K_BACKSPACE:
            return -2
        if event.key == K_KP0:
          return 0
        if event.key == K_KP1:
          return 1
        if event.key == K_KP2:
          return 2
        if event.key == K_KP3:
          return 3
        if event.key == K_KP4:
          return 4
        if event.key == K_KP5:
          return 5
        if event.key == K_KP6:
          return 6
        if event.key == K_KP7:
          return 7
        if event.key == K_KP8:
          return 8
        if event.key == K_KP9:
          return 9

  

#To leave at the end
initialisation()
