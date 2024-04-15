
""" thorns.py
    plant growing game
    Brielle"""

import pygame, simpleGE

class Sun(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("sunshine.png")
        self.setSize(150, 150)
        self.position = (145, 275)
        
        

class Moon(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("moon.png")
        self.setSize(150, 150)
        self.position = (495, 300)
       
        
class ChoiceOne(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("invisible.png")
        self.setSize(150, 150)
        self.position = (145, 275)
        self.moveSpeed = 0
        
    def process(self):
        if self.clicked:
            self.moveSpeed = 5
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
        if self.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
        
            #add A and D later
           # if self.isKeyPressed(pygame.K_a):
             #   self.x -= self.moveSpeed
            #if self.isKeyPressed(pygame.K_d):
              #  self.x += self.moveSpeed
        

        
class ChoiceTwo(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("invisible.png")
        self.setSize(150, 150)
        self.position = (495, 300)
        self.moveSpeed = 0
    def process(self):
         if self.clicked:
             self.moveSpeed = 5
         if self.isKeyPressed(pygame.K_LEFT):
             self.x -= self.moveSpeed
         if self.isKeyPressed(pygame.K_RIGHT):
             self.x += self.moveSpeed
         if self.isKeyPressed(pygame.K_UP):
             self.y -= self.moveSpeed
         if self.isKeyPressed(pygame.K_DOWN):
             self.y += self.moveSpeed

        
class Nothing(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("invisible.png")
        self.setSize(100,100)
        self.position = (550, 75)

class Seed(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seed.png") #add growing scre
        self.setSize(150, 150)
        self.position = (320, 75)
        
    def process(self):
        if self.isKeyPressed(pygame.K_SPACE):
            self.dy = 5
        
            
    
        
class FlowerPot(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("flowerPot.png")
        self.setSize(150, 150)
        self.position = (320, 400)
        
   # def process(self):
     #   if self.


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("grow.png")
       
        self.seed = Seed(self)
        self.flowerPot = FlowerPot(self)
        #self.waterLabel = WaterLabel()
        #self.chooseWaterLabel = ChooseWaterLabel()
       # self.chooseAcidLabel = ChooseAcidLabel()
        #self.chooseNothingLabel = ChooseNothingLabel()
        self.choiceOne = ChoiceOne(self)
        self.choiceTwo = ChoiceTwo(self)
        self.nothing = Nothing(self)
        self.sun = Sun(self)
        self.moon = Moon(self)
        
        
      #  self.waterLabel = simpleGE.MultiLabel()
      #  self.waterLabel.textLines = [
      #      "Use the spacebar to drop the seed",
       #     "then click on one option.",
        #    " Use the arrow keys to move it",
         #   "to the flower pot."
          #  ]
        #self.waterLabel.center = (320, 75)
        #self.waterLabel.size = (350, 150)
        
        self.sprites = [self.nothing,
                        self.seed,
                        self.flowerPot,
                        self.choiceOne,
                        self.choiceTwo,
                        self.sun,
                        self.moon
                            #self.storm
                        
                        
                        
                        
                        ]
        
        self.plant = []
        self.sun.hide()
        self.moon.hide()
    def process(self):
       # plant = []
        if self.seed.collidesWith(self.flowerPot):
            
            self.seed.position = (0, 0)
            self.seed.setImage("invisible.png")
            self.choiceOne.setImage("wateringCan.png")
            self.choiceOne.setSize(150, 150)
            self.choiceTwo.setImage("acid.png")
            self.choiceTwo.setSize(150, 150)
            self.nothing.setImage("nothing.png")
            self.nothing.setSize(100, 100)
    
        if self.choiceOne.collidesWith(self.flowerPot):
            self.plant.append("3")
            self.choiceOne.position = (145, 275)
            self.choiceOne.setImage("gnomesoil.png")
            self.choiceOne.moveSpeed = 0
            self.choiceTwo.setImage("rawmeat.png")
            print(f"{self.plant}")
        if self.plant == ["3", "3"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            self.moon.show()
        if self.plant == ["7", "3"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            self.moon.show()
        if self.plant == ["1", "3"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            self.moon.show()
            
        if self.choiceTwo.collidesWith(self.flowerPot):
            self.plant.append("7")
            self.choiceOne.setImage("gnomesoil.png")
            self.choiceTwo.moveSpeed = 0
            self.choiceTwo.setImage("rawmeat.png")
            self.choiceTwo.position = (495, 275)
        if self.plant == ["7", "7"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            self.moon.show()
        if self.plant == ["3", "7"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            self.moon.show()
        if self.plant == ["1", "7"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            self.moon.show()
        
            print(f"{self.plant}")
        if self.nothing.clicked:
            self.plant.append("1")
            self.nothing.position = (550, 75)
            self.choiceOne.setImage("gnomesoil.png")
            self.nothing.moveSpeed = 0
            self.choiceTwo.setImage("rawmeat.png")
        if self.plant == ["1", "1"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            self.moon.show()
        if self.plant == ["3", "1"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            self.moon.show()
        if self.plant == ["7", "1"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.show()
            
            self.moon.show()
            
        #if self.sun.clicked:
            
            
     
        
          
            

        #newimage over sprite OR hide and put new images over top

#class NextGame(simpleGE.Scene):
 #   def __init__(self):
  #      super().__init__()   
  #      self.setImage("grow.png")
        
   #     self.flowerPot = FlowerPot(self)
        
   #     self.sprites = [self.flowerPot,
                        
                        
                    
                      #  ]
            
            
    
        
        
        
def main():
   # keepGoing = True
   # Game.start()
   # while keepGoing:
     game =Game()
     game.start()
        
        
        #game.start()
      #  print(instructions.response)
    
      #  if Game.response == "Next":    
        #    nextGame = NextGame()
       #     nextGame.start()
            
      #  else:
        #    keepGoing = False
  #
if __name__ == "__main__":
    main()