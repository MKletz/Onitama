class Piece():
    
    def __init__(self,color,is_master):
        self.is_master = is_master
        self.color = color

    def eliminate(self):
        if self.is_master:
            print("you're dead Jim.")
        else:
            print("I'm dead Jim.")