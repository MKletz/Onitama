class Tile():

    def __init__(self):
        self.occupied = False
        self.occupying_piece = None
        self.x = None
        self.y = None
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

    def move_to(self,piece,from_tile):
        if self.get_occupying_color() == piece.color:
            raise ValueError('You already have a piece on that tile!')
        elif self.occupied and self.get_occupying_color() != piece.color:
            self.occupying_piece.eliminate()
        else:
            self.occupied = True
            self.occupying_piece = piece
            from_tile.move_from()