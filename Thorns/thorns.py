
""" thorns.py
    plant growing game
    Brielle"""

import pygame, simpleGE




        
class Sun(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("invisible.png")
        self.setSize(150, 150)
        self.position = (145, 275)
        self.moveSpeed = 0
    
    def reset(self):
        self.setSize(150, 150)
        self.position = (145, 275)
        self.moveSpeed = 0
        self.setImage("sunshine.png")
        
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
    

class Moon(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("invisible.png")
        self.setSize(150, 150)
        self.position = (1, 1)
        self.moveSpeed = 0
    
    def reset(self):
        self.setSize(150, 150)
        self.position = (495, 300)
        self.moveSpeed = 5
        self.setImage("moon.png")
        
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

    
class ChoiceOne(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("invisible.png")
        self.setSize(150, 150)
        self.position = (145, 275)
        self.moveSpeed = 0
    
    def reset(self):
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
        
    def reset(self):
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
        self.setSize(50, 50)
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
        self.choiceOne = ChoiceOne(self)
        self.choiceTwo = ChoiceTwo(self)
        self.nothing = Nothing(self)
        self.sun = Sun(self)
        self.moon = Moon(self)
        
        self.btnGrow = simpleGE.Button()
        self.btnGrow.text = "Grow!"
        self.btnGrow.center = (400, 240)
        self.btnGrow.hide()
        
      
        
        self.sprites = [self.flowerPot,
                        self.sun,
                        self.moon,
                        self.nothing,
                        self.seed,
                        self.btnGrow,
                        self.choiceOne,
                        self.choiceTwo,
                        
                           
                        
                        
                        
                        
                        ]
        
        self.plant = []
        
    def process(self):
       
        
        if self.seed.collidesWith(self.flowerPot): 
            self.seed.hide()
            
            self.choiceOne.reset()
            self.choiceOne.setImage("wateringCan.png")
            
            self.choiceTwo.reset()
            self.choiceTwo.setImage("acid.png")
            
            self.nothing.setImage("nothing.png")
         
    
        if self.choiceOne.collidesWith(self.flowerPot):
            
            self.plant.append("3")
        
            self.choiceOne.reset()
            self.choiceOne.setImage("gnomesoil.png")
            
            self.choiceTwo.reset()
            self.choiceTwo.setImage("rawmeat.png")
            print(f"{self.plant}")
            
        
        elif self.choiceTwo.collidesWith(self.flowerPot):
            
            self.plant.append("7")
            
            self.choiceOne.reset()
            self.choiceOne.setImage("gnomesoil.png")
            
            self.nothing.hide()
                
            self.choiceTwo.reset()
            self.choiceTwo.setImage("rawmeat.png")
            
            print(f"{self.plant}")
            
            
        elif self.nothing.clicked:
            self.plant.append("1")
            
            self.choiceOne.reset()
            self.choiceOne.setImage("gnomesoil.png")
                    
            self.choiceTwo.reset()
            self.choiceTwo.setImage("rawmeat.png")
            
            print(f"{self.plant}")
            
        elif self.plant == ["1", "1"] or self.plant == ["1", "3"] or self.plant == ["1", "7"] or self.plant == ["3", "1"] or self.plant == ["3", "3"] or self.plant == ["3", "7"] or self.plant == ["7", "1"] or self.plant == ["7", "3"] or self.plant == ["7", "7"]:
            self.choiceOne.hide()
            self.choiceTwo.hide()
            self.nothing.hide()
            self.sun.reset()
            self.moon.reset()
            
            if self.sun.clicked:
                self.plant.append("1")
                print(f"{self.plant}")
                self.sun.hide()
                self.moon.hide()
                self.btnGrow.show()
            elif self.moon.clicked:
                self.plant.append("7")
                print(f"{self.plant}")
                self.moon.hide()
                self.sun.hide()
                self.btnGrow.show()
                
        if self.btnGrow.clicked:
            print("grow clicked")
            self.stop()
                
        
class GetPlant(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("introScreenDraft.png")
        
        self.rename = simpleGE.MultiLabel()
        self.rename.textLines = [
        "Congrats on your plant!",  
        "Would you like to rename this plant?"
            ]
        
        self.rename.center = (320, 100)
        self.rename.size = (400, 150)
        self.sprites = [self.rename]
        
        
        
        
        
        
def main():
  
    game = Game()
    game.start()
        
    getPlant = GetPlant()
    getPlant.start()
        
if __name__ == "__main__":
    main()