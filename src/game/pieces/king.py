import itertools
from ..board.board import Board

#creation of the king class
class King:
    def __init__(self,color,file,row,first_move=1):
        self.color = color #lets code 'w' for whites and 'b' for blacks
        self.piece_type = 'K'
        self.file = file
        self.row = row
        self.first_move = first_move


    def move(self,move):
        self.file=move[0]
        self.row=move[1]
        if self.first_move == 1:
            self.first_move = 0

    def vision(self,board):
        vision=[]
        # a king can go anywhere 1 case distance if there is no piece of his color on it or if no opposite color piece vision on it
        for i,j in itertools.product([-1,0,1], [-1,0,1]):
            if i==0 and j==0:
                pass
            else:
                if self.file+i<1 or self.file+i>8 or self.row+j<1 or self.row+j>8:
                    pass
                else:
                    if [self.file+i,self.row+j] in board.get_one_color_position(self.color):
                        pass
                    else:
                        vision.append([self.file+i,self.row+j])
                        # the case of a square occupied by an opposite color piece vision is handled by projecting one move
                        #into the future to make sure the move is legal (king not checked), same as for pinned pieces

        # now we code castling
        if self.color=='w':
            if self.first_move==1:

                #left castling
                piece = board.get_piece_from_position([1,1])
                if piece!=0:
                    if piece.piece_type=='r':
                        if piece.first_move==1:
                            if board.is_checked()!='w':
                                black_pieces_vision=[]
                                all_pieces_position = board.get_one_color_position('b')+board.get_one_color_position('w')
                                for piece in board.pieces['b']:
                                    black_pieces_vision+=piece.vision(board)
                                if [4,1] not in black_pieces_vision and [2,1] not in all_pieces_position and [3,1] not in all_pieces_position and [4,1] not in all_pieces_position:
                                    vision.append([3,1])

                #right castling
                piece = board.get_piece_from_position([8,1])
                if piece!=0:
                    if piece.piece_type=='r':
                        if piece.first_move==1:
                            if board.is_checked()!='w':
                                black_pieces_vision=[]
                                all_pieces_position = board.get_one_color_position('b')+board.get_one_color_position('w')
                                for piece in board.pieces['b']:
                                    black_pieces_vision+=piece.vision(board)
                                if [6,1] not in black_pieces_vision and [6,1] not in all_pieces_position and [7,1] not in all_pieces_position:
                                    vision.append([7,1])

        else:
            if self.first_move==1:

                #left castling
                piece = board.get_piece_from_position([1,8])
                if piece!=0:
                    if piece.piece_type=='r':
                        if piece.first_move==1:
                            if board.is_checked()!='b':
                                white_pieces_vision=[]
                                all_pieces_position = board.get_one_color_position('b')+board.get_one_color_position('w')
                                for piece in board.pieces['w']:
                                    white_pieces_vision+=piece.vision(board)
                                if [4,8] not in white_pieces_vision and [2,8] not in all_pieces_position and [3,8] not in all_pieces_position and [4,8] not in all_pieces_position:
                                    vision.append([3,8])

                #right castling
                piece = board.get_piece_from_position([8,8])
                if piece!=0:
                    if piece.piece_type=='r':
                        if piece.first_move==1:
                            if board.is_checked()!='b':
                                white_pieces_vision=[]
                                all_pieces_position = board.get_one_color_position('b')+board.get_one_color_position('w')
                                for piece in board.pieces['w']:
                                    white_pieces_vision+=piece.vision(board)
                                if [6,8] not in black_pieces_vision and [6,8] not in all_pieces_position and [7,8] not in all_pieces_position:
                                    vision.append([7,8])
        return vision
