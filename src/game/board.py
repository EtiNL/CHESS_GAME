from .pawn import Pawn
from .king import King
from .queen import Queen
from .bishop import Bishop
from .knight import Knight
from .rook import Rook



class Board:
    def __init__(self,newgame,position):
        self.moves = []
        if newgame:

            #create the white pieces
            #wAp = white A pawn ...
            wAp,wBp,wCp,wDp,wEp,wFp,wGp,wHp=Pawn('w',1,2),Pawn('w',2,2),Pawn('w',3,2),Pawn('w',4,2),Pawn('w',5,2),Pawn('w',6,2),Pawn('w',7,2),Pawn('w',8,2)
            #wwb = white bishop on the white square
            wwb,wbb=Bishop('w',6,1),Bishop('w',3,1)
            #wk1 = white knight 1
            wk1,wk2=Knight('w',7,1),Knight('w',2,1)
            #wr1 = white rook 1
            wr1,wr2=Rook('w',1,1),Rook('w',8,1)
            wQ=Queen('w',4,1)
            wK=King('w',5,1)

            #create the black pieces
            bAp,bBp,bCp,bDp,bEp,bFp,bGp,bHp=Pawn('b',1,7),Pawn('b',2,7),Pawn('b',3,7),Pawn('b',4,7),Pawn('b',5,7),Pawn('b',6,7),Pawn('b',7,7),Pawn('b',8,7)
            bwb,bbb=Bishop('b',6,8),Bishop('b',3,8)
            bk1,bk2=Knight('b',7,8),Knight('b',2,8)
            br1,br2=Rook('b',1,8),Rook('b',8,8)
            bQ=Queen('b',4,8)
            bK=King('b',5,8)

            self.pieces = {'w':[wAp,wBp,wCp,wDp,wEp,wFp,wGp,wHp,wwb,wbb,wk1,wk2,wr1,wr2,wQ,wK],
                           'b':[bAp,bBp,bCp,bDp,bEp,bFp,bGp,bHp,bwb,bbb,bk1,bk2,br1,br2,bQ,bK]}


        else:
            self.pieces = {'w':[],
                           'b':[]}
            #position=[[color,type of piece, file, row, first_move (if r or K)]... ]
            for pos in position:
                if pos[1]=='p':
                    self.pieces[pos[0]].append(Pawn(pos[0],pos[2],pos[3]))
                elif pos[1]=='b':
                    self.pieces[pos[0]].append(Bishop(pos[0],pos[2],pos[3]))
                elif pos[1]=='k':
                    self.pieces[pos[0]].append(Knight(pos[0],pos[2],pos[3]))
                elif pos[1]=='r':
                    self.pieces[pos[0]].append(Rook(pos[0],pos[2],pos[3]))
                elif pos[1]=='Q':
                    self.pieces[pos[0]].append(Queen(pos[0],pos[2],pos[3]))
                else:
                    self.pieces[pos[0]].append(King(pos[0],pos[2],pos[3]))

    def get_entire_position(self):
            position=[]

            for piece in self.pieces['w']:
                if piece.piece_type=='r' or piece.piece_type=='K':
                    position.append([piece.color,piece.piece_type,piece.file,piece.row,piece.first_move])
                else:
                    position.append([piece.color,piece.piece_type,piece.file,piece.row])

            for piece in self.pieces['b']:
                if piece.piece_type=='r' or piece.piece_type=='K':
                    position.append([piece.color,piece.piece_type,piece.file,piece.row,piece.first_move])
                else:
                    position.append([piece.color,piece.piece_type,piece.file,piece.row])

            return position

    def get_one_color_position(self,color):
            position=[]
            for piece in self.pieces[color]:
                position.append([piece.file,piece.row])
            return position

    def get_piece_from_position(self,pos):
        #pos = [piece.file, piece.row]

        for piece in self.pieces['w']:
            if piece.file==pos[0] and piece.row==pos[1]:
                return piece
        for piece in self.pieces['b']:
            if piece.file==pos[0] and piece.row==pos[1]:
                return piece

        return 0 #if no piece found in this position it returns 0

    def is_checked(self):

        #getting the white king position
        for piece in self.pieces['w']:
            if piece.piece_type=='K':
                break
        white_king_pos = [piece.file,piece.row]

        #looking for checks
        for piece in self.pieces['b']:
            if piece.piece_type!='K':
                vision = piece.vision(self)
                if white_king_pos in vision:
                    return 'w' #returns 'w' if the white king is checked

        #getting the black king position
        for piece in self.pieces['b']:
            if piece.piece_type=='K':
                break
        black_king_pos = [piece.file,piece.row]

        #looking for checks
        for piece in self.pieces['w']:
            if piece.piece_type!='K':
                vision = piece.vision(self)
                if black_king_pos in vision:
                    return 'b' #returns 'b' if the black king is checked

        return 0 # if no one is checked

    def possible_moves(self,color):
        possible_moves = [] #[[piece,move],...]

        for piece in self.pieces[color]:
            for move in piece.vision(self):
                position_to_test = self.get_entire_position()

                for i,pos in enumerate(position_to_test):
                    if pos==[color,piece.piece_type,piece.file,piece.row]:
                        break

                position_to_test[i]=[color,piece.piece_type,move[0],move[1]]
                Position_to_test = Board(0,position_to_test)
                if color == 'w':
                    if Position_to_test.is_checked()!='w':
                        possible_moves.append([piece,move])
                else:
                    if Position_to_test.is_checked()!='b':
                        possible_moves.append([piece,move])

                Position_to_test.delete_all_pieces()
                del Position_to_test

        return possible_moves

    def delete_all_pieces(self):
        del self.pieces['w']
        del self.pieces['b']

    def move(self,piece,move):
        if move not in piece.vision(self):
            return 0 #not a legal move
        else:
            position_to_test = self.get_entire_position()

            if piece.piece_type=='K' or piece.piece_type=='r':
                i = position_to_test.index([piece.color,piece.piece_type,piece.file,piece.row,piece.first_move])
                position_to_test[i]=[piece.color,piece.piece_type,move[0],move[1],piece.first_move]
            else:
                i = position_to_test.index([piece.color,piece.piece_type,piece.file,piece.row])
                position_to_test[i]=[piece.color,piece.piece_type,move[0],move[1]]
            Position_to_test = Board(0,position_to_test)
            if piece.color == 'w'and Position_to_test.is_checked()=='w':
                return 0
            else:
                if Position_to_test.is_checked()=='b':
                    return 0

            Position_to_test.delete_all_pieces()
            del Position_to_test

            # we have handled all cases of illegal moves
            # Now we have to handle the case of capture (with en passant) and castling

            if piece.color =='w':
                if move in self.get_one_color_position('b'):
                    taken_piece = self.get_piece_from_position(move)
                    self.pieces['b'].remove(taken_piece)
                    taken_piece.state = 0
                    self.moves.append(([piece.file,piece.row],move))
                    piece.move(move)

                    print('take')
                # en passant
                elif piece.piece_type == 'p' and move[0]!= piece.file:
                    taken_piece = self.get_piece_from_position([move[0],move[1]-1])
                    self.pieces['b'].remove(taken_piece)
                    taken_piece.state = 0
                    self.moves.append(([piece.file,piece.row],move))
                    piece.move(move)
                    print('en passant !')

                else:
                    if piece.piece_type=='K' and (move[0]-piece.file<-1 or move[0]-piece.file>1):
                        position_to_test = self.get_entire_position()

                        i = position_to_test.index([piece.color,piece.piece_type,piece.file,piece.row,piece.first_move])
                        if move[0]==7: #right castling
                            position_to_test[i]=[piece.color,piece.piece_type,6,1,1]
                            Position_to_test = Board(0,position_to_test)
                            if Position_to_test.is_checked()=='w':
                                Position_to_test.delete_all_pieces()
                                del Position_to_test
                                return 0
                            rook = self.get_piece_from_position([8,1])
                            rook.move([6,1])
                            self.moves.append(([piece.file,piece.row],move))
                            piece.move(move)
                        else: #left castling
                            position_to_test[i]=[piece.color,piece.piece_type,4,1,1]
                            Position_to_test = Board(0,position_to_test)
                            if Position_to_test.is_checked()=='w':
                                Position_to_test.delete_all_pieces()
                                del Position_to_test
                                return 0
                            rook = self.get_piece_from_position([1,1])
                            rook.move([4,1])
                            self.moves.append(([piece.file,piece.row],move))
                            piece.move(move)
                    else:
                        self.moves.append(([piece.file,piece.row],move))
                        piece.move(move)
            else:
                if move in self.get_one_color_position('w'):
                    taken_piece = self.get_piece_from_position(move)
                    self.pieces['w'].remove(taken_piece)
                    taken_piece.state = 0
                    self.moves.append(([piece.file,piece.row],move))
                    piece.move(move)
                    print('take')
                elif piece.piece_type == 'p' and move[0]!= piece.file:
                    taken_piece = self.get_piece_from_position([move[0],move[1]+1])
                    self.pieces['w'].remove(taken_piece)
                    taken_piece.state = 0
                    self.moves.append(([piece.file,piece.row],move))
                    piece.move(move)
                    print('en passant !')
                else:
                    if piece.piece_type=='K' and (move[0]-piece.file<-1 or move[0]-piece.file>1):
                        position_to_test = self.get_entire_position()

                        i = position_to_test.index([piece.color,piece.piece_type,piece.file,piece.row,piece.first_move])
                        if move[0]==7: #right castling
                            position_to_test[i]=[piece.color,piece.piece_type,6,8,1]
                            Position_to_test = Board(0,position_to_test)
                            if Position_to_test.is_checked()=='b':
                                Position_to_test.delete_all_pieces()
                                del Position_to_test
                                return 0
                            rook = self.get_piece_from_position([8,8])
                            rook.move([6,8])
                            self.moves.append(([piece.file,piece.row],move))
                            piece.move(move)
                        else: #left castling
                            position_to_test[i]=[piece.color,piece.piece_type,4,8,1]
                            Position_to_test = Board(0,position_to_test)
                            if Position_to_test.is_checked()=='b':
                                Position_to_test.delete_all_pieces()
                                del Position_to_test
                                return 0
                            rook = self.get_piece_from_position([1,8])
                            rook.move([4,8])
                            self.moves.append(([piece.file,piece.row],move))
                            piece.move(move)
                    else:
                        self.moves.append(([piece.file,piece.row],move))
                        piece.move(move)


            # Then the case of promotion for now only in queen
            if piece.color =='w':
                if piece.piece_type=='p' and piece.row==8:
                    self.pieces['w'].remove(piece)
                    self.pieces['w'].append(Queen('w',piece.file,piece.row))
                    piece.state = 0

            else:
                if piece.piece_type=='p' and piece.row==1:
                    self.pieces['b'].remove(piece)
                    self.pieces['b'].append(Queen('b',piece.file,piece.row))
                    piece.state = 0
