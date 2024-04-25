
""" thorns.py
    plant growing game
    Brielle"""

import pygame, simpleGE, random




        
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
class Spacebar(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Press spacebar"
        self.center = (450, 75)
    

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
        
        self.spacebar = Spacebar()
        
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
                        self.spacebar
                           
                        
                        
                        
                        
                        ]
        
        self.plant = []
        
    def process(self):
       
        
        if self.seed.collidesWith(self.flowerPot): 
            self.seed.hide()
            self.spacebar.hide()
            
            self.choiceOne.reset()
            self.choiceOne.setImage("wateringCan.png")
            
            self.choiceTwo.reset()
            self.choiceTwo.setImage("acid.png")
            
            self.nothing.setImage("nothing.png")
         
    
        if self.choiceOne.clicked:
            
            self.plant.append("3")
        
            self.choiceOne.reset()
            self.choiceOne.setImage("gnomesoil.png")
            
            self.choiceTwo.reset()
            self.choiceTwo.setImage("rawmeat.png")
            print(f"{self.plant}")
            
        
        if self.choiceTwo.clicked:
            
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
        
class HPLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "HP: 30"
        self.center = (100, 30)
        
class EnemyHPLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "HP: 50"
        self.center = (540, 30)
        
class GetPlant(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("introScreenDraft.png")
        
        self.rename = simpleGE.MultiLabel()
        self.rename.textLines = [
        "Congrats on your plant!",  
        "Click on it to view your",
        "opponent, then click the",
        "enemy to fight it!"
            ]
        
        self.rename.center = (320, 100)
        self.rename.size = (400, 150)
        
      
        
        self.plantType = PlantType(self)
        self.enemy = Enemy(self)
        
        self.hPLabel = HPLabel()
        self.hP = 30
        
        self.enemyHPLabel = EnemyHPLabel()
        self.enemyHP = 50
        
        self.sprites = [self.plantType,
                        self.rename,
                        self.enemy,
                        self.hPLabel,
                        self.enemyHPLabel
                        ]
        
        
        
       
    def process(self):
            if self.plantType.clicked:
                self.rename.hide()
                self.enemy.show()
                
           # if self.isKeyPressed(pygame.K_SPACE):
                
                 
                
            if self.enemy.clicked:
                if random.randint(1, 100) < 70:
                    enemyDamage = random.randint(1, 5)
                    self.enemyHP -= enemyDamage 
                    self.enemyHPLabel.text = f"Enemy HP: {self.enemyHP}"
                    self.hPLabel.text = f"HP: {self.hP}"
                    
                if random.randint(1, 100) < 30:
                    plantTypeDamage = random.randint(1, 7)
                    self.hP -= plantTypeDamage
                    self.hPLabel.text = f"HP: {self.hP}"
                    if self.enemyHP <= 0:
                            #self.congratulations.show()
                        print("congratulations")
                            #keepGoing = False
                    if self.hP <= 0:
                        print("I can't believe you lost...")
                            #self.loser.show()
                            #keepGoing = False
                
                    
                #create loser and congratulations sprite, find a way to loop, create gnome soil, write game document
                        
                    
                    
            
        
        
           
      
            
        
        
class Enemy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        randomEnemy = random.randint(0, 14)
        self.setImage(f"{randomEnemy}.png")
        self.position = (550, 240)
        self.setSize = (50, 50) 
        self.hide()          
        
      
        
   
            
class PlantType(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        image = random.randint(0, 14)
        self.setImage(f"{image}.png")
        print(f"{image}")
        self.setSize(200, 200)
        self.position = (100, 350)
        
class Intro(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("introScreen.png")
        
        self.response = "Quit"
        
        
        self.howTo = simpleGE.MultiLabel()
        self.howTo.textLines = [
            "Welcome to Thorns!",
            "Click on one of each",
            "options to create the",
            "toughest plant!"
            ]
        self.howTo.center = (320, 400)
        self.howTo.size = (200, 150)
    
        
    
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 30)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 30)
        
       
        
        self.sprites = [self.howTo,
                        self.btnPlay,
                        self.btnQuit,
                        
                        ]
        
      
    
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
       

    

   

        
        
        
        
        
        
        
        
        
        
def main():
    keepGoing = True
    while keepGoing:
        intro = Intro()
        intro.start()
        if intro.response == "Play":
            game = Game()
            game.start()
       
    
            getPlant = GetPlant()
            getPlant.start()
            
        else: 
            keepGoing = False
    
    
        
if __name__ == "__main__":
    main()