import pygame, simpleGE
""" thorns.py
    plant growing game
    Brielle"""

import pygame, simpleGE

class Seed(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seed.png") #add growing scre
        self.setSize(150, 150)
        self.position = (320, 240)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("grow.png")
       
        self.seed = Seed(self)
        
        self.sprites = [self.seed]
        
        
def main():
  game = Game()
  game.start()
  
if __name__ == "__main__":
    main()