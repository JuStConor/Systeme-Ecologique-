class Mouton (gain_nourriture,position_x,position_y,energie,taux_reproduction):
    def variationEnergie(i,j):
        energie = 0
        if i != 0:
            energie += 1
        else:
            gain_nourriture = gain_nourriture + 1
        return energie
    def deplacement(self):
        
        
    def place_mouton(self,i,j):
