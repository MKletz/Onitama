class Piece():
    
    def __init__(self):
        self.is_master = False
        self.color = None

    def eliminate(self):
        if self.is_master:
            print("you're dead Jim.")
        else:
            print("I'm dead Jim.")