class Tile():

    def __init__(self,x,y,piece):
        self.occupying_piece = piece
        if self.occupying_piece != None:
            self.occupied = True
        else:
            self.occupied = False
        self.x = x
        self.y = y
        self.image = "Default.png"

    def get_occupying_color(self):
        if self.occupied:
            return self.occupying_piece.color
        else:
            return None
    
    def get_occupying_is_master(self):
        if self.occupying_piece != None:
            return self.occupying_piece.is_master
        else:
            return None

    def move_from(self):
        self.occupied = False
        self.occupying_piece = None

    def move_to(self,from_tile):
        if self.get_occupying_color() == from_tile.get_occupying_color():
            raise ValueError('You already have a piece on that tile!')
        elif self.occupied and self.get_occupying_color() != from_tile.get_occupying_color():
            self.occupying_piece.eliminate()
        else:
            self.occupied = True
            self.occupying_piece = from_tile.occupying_piece
            from_tile.move_from()

    def set_starting_tile(self,piece):
        self.occupied = True
        self.occupying_piece = piece