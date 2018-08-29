from Piece import *
from Tile import *

class Board():

    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.player1_color = 'Red'
        self.player2_color = 'Blue'
        self.tiles = []
        for row in range(height):    
            column = 0
            while column < width:
                if row == 0:
                    self.tiles.append(Tile(column,row,Piece(self.player1_color,False)))
                elif row == self.height - 1:
                    self.tiles.append(Tile(column,row,Piece(self.player2_color,False)))
                else:
                    self.tiles.append(Tile(column,row,None))
                column += 1

    def set_masters(self,player1_x,player1_y,player2_x,player2_y):
        for tile in self.tiles:
            if (tile.x == player1_x and tile.y == player1_y) or (tile.x == player2_x and tile.y == player2_y):
                tile.occupying_piece.is_master = True