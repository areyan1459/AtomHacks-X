from sre_constants import REPEAT
import pygame 
import sys
import random
from pygame import draw
from pygame.draw import rect
from pygame.event import wait
from pygame.locals import QUIT


ship = pygame.image.load("New Piskel (5).png")
shipsize = (50, 50)
ship = pygame.transform.scale(ship, shipsize)

orb1pos = int(random.random()*1000), int(random.random()*1000)
orb2pos = int(random.random()*1000), int(random.random()*1000)
orb3pos = int(random.random()*1000), int(random.random()*1000)
orb4pos = int(random.random()*1000), int(random.random()*1000)
orb5pos = int(random.random()*1000), int(random.random()*1000)

# Variables 
energy = 10000
screen_width = 800
screen_height = 600



#Colors
WHITE = (255, 255, 255)
RED = (255,0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)



#Initalize Py
pygame.init()
energyUse = 25
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
shipposx = 0
shipposy = 0


# Energy Orb Import
energyLogo1 = pygame.image.load('Energy.png')
energyLogo1 = pygame.transform.scale(energyLogo1, (50, 50))
energyLogo2 = pygame.image.load('Energy.png')
energyLogo2 = pygame.transform.scale(energyLogo2, (50, 50))
energyLogo3 = pygame.image.load('Energy.png')
energyLogo3 = pygame.transform.scale(energyLogo3, (50, 50))
energyLogo4 = pygame.image.load('Energy.png')
energyLogo4 = pygame.transform.scale(energyLogo4, (50, 50))
energyLogo5 = pygame.image.load('Energy.png')
energyLogo5 = pygame.transform.scale(energyLogo5, (50, 50))
# Background Import
background = pygame.image.load('pixilart-sprite.png')


# Energy Bar Updates
def energy_bar(energy):
  pygame.draw.rect(screen, WHITE, [20, 20, 220, 25])
  if(energy > 200):
    energy = 200
  if (energy < 0):
    energy = 0
  pygame.draw.rect(screen, YELLOW, [30, 25, energy, 15])    
current = 0




# main area
while True:
  for event in pygame.event.get():
    display = pygame.Rect(350,000,200,100)


  
# Movement
  keys = pygame.key.get_pressed()
  if keys[pygame.K_d]:
     energy -= 2
     shipposx += 10
     screen.fill((0,0,0))
  if keys[pygame.K_a]:
     energy -= 2
     shipposx -= 10
     screen.fill((0,0,0))
  if keys[pygame.K_w]:
     energy -= 2
     shipposy -= 10
     screen.fill((0,0,0))
  if keys[pygame.K_s]:
     energy -= 2
     shipposy += 10
     screen.fill((0,0,0))



  
  # Objects
  # Background Load
  screen.blit(background, (0,0))



  screen.blit(energyLogo1, orb1pos)
  screen.blit(energyLogo2, orb2pos)
  screen.blit(energyLogo3, orb4pos)
  screen.blit(energyLogo4, orb4pos)
  screen.blit(energyLogo5, orb5pos)

  shippos = (shipposx, shipposy)
  
  if(abs(shippos[0] - orb1pos[0]) <= 50 and abs(shippos[1] - orb1pos[1]) <= 50):
    energy+=200
    orb1pos = int(random.random()*1000), int(random.random()*1000)
  if(abs(shippos[0] - orb1pos[0]) <= 50 and abs(shippos[1] - orb1pos[1]) <= 50):
    energy+= 200
    orb2pos = int(random.random()*1000), int(random.random()*1000)
  if(abs(shippos[0] - orb1pos[0]) <= 50 and abs(shippos[1] - orb1pos[1]) <= 50):
    energy+= 200
    orb3pos = int(random.random()*1000), int(random.random()*1000)
  if(abs(shippos[0] - orb1pos[0]) <= 50 and abs(shippos[1] - orb1pos[1]) <= 50):
    energy+= 200
    orb4pos = int(random.random()*1000), int(random.random()*1000)
  if(abs(shippos[0] - orb1pos[0]) <= 50 and abs(shippos[1] - orb1pos[1]) <= 50):
    energy+= 200
    orb5pos = int(random.random()*1000), int(random.random()*1000)






  
  # Energy Bar Call
  energy_bar(energy)

  
  screen.blit(ship, shippos)

  if energy == 0:
    screen.fill((0,0,0))
    break
  
  clock.tick(60)



  
  # End/Update
  if event.type == QUIT:
    pygame.quit()
    sys.exit()
  pygame.display.flip()
