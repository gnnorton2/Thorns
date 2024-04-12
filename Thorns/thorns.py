
""" thorns.py
    plant growing game
    Brielle"""

import pygame, simpleGE

#create labels for plant-growing categories, classes
class WaterLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "What will you water your plant with?"
        self.center = (320, 50) #make this bigger
        
class ChooseWaterLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Water"
        self.center = (145, 213)
        
class WateringCan(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("wateringCan.png")
        self.setSize(150, 150)
        self.position = (145, 275)
        
class ChooseAcidLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Acid"
        self.center = (495, 213)
        
class AcidVial(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("acid.png")
        self.setSize(150, 150)
        self.position = (495, 300)
        
class ChooseNothingLabel(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Nothing"
        self.center = (320, 150)
        
class Nothing(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("nothing.png")
        self.setSize(150,150)
        self.position = (320, 250)

class Seed(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("seed.png") #add growing scre
        self.setSize(150, 150)
        self.position = (320, 240)
        
   # def process(self):
     #   if self.

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("grow.png")
       
        self.seed = Seed(self)
        self.waterLabel = WaterLabel()
        self.chooseWaterLabel = ChooseWaterLabel()
        self.chooseAcidLabel = ChooseAcidLabel()
        self.chooseNothingLabel = ChooseNothingLabel()
        self.wateringCan = WateringCan(self)
        self.acidVial = AcidVial(self)
        self.nothing = Nothing(self)
        
        self.sprites = [self.seed,
                        self.waterLabel,
                        self.chooseWaterLabel,
                        self.chooseAcidLabel,
                        self.chooseNothingLabel,
                        self.wateringCan,
                        self.acidVial,
                        self.nothing]
        
        
        
def main():
  game = Game()
  game.start()
  
if __name__ == "__main__":
    main()