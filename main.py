from src.game import board
from src.graphic_interface import graphic_interface

game = board.Board(1,0)
# position_to_test = [['w', 'p', 1, 2], ['w', 'p', 2, 2], ['w', 'p', 3, 2], ['w', 'p', 4, 2], ['w', 'p', 4, 5], ['w', 'p', 6, 2], ['w', 'p', 7, 2], ['w', 'p', 8, 2], ['w', 'b', 6, 1], ['w', 'b', 3, 1], ['w', 'k', 7, 1], ['w', 'k', 2, 1], ['w', 'r', 1, 1, 1], ['w', 'r', 8, 1, 1], ['w', 'Q', 4, 1], ['w', 'K', 5, 1, 1], ['b', 'p', 1, 7], ['b', 'p', 2, 7], ['b', 'p', 3, 7], ['b', 'p', 5, 7], ['b', 'p', 6, 7], ['b', 'p', 7, 7], ['b', 'p', 8, 7], ['b', 'b', 6, 8], ['b', 'b', 3, 8], ['b', 'k', 7, 8], ['b', 'k', 2, 8], ['b', 'r', 1, 8, 1], ['b', 'r', 8, 8, 1], ['b', 'Q', 4, 8], ['b', 'K', 5, 8, 1]]
# game = board.Board(0,position_to_test)
"A_pawn = game.get_piece_from_position([1,2])"
"game.move(A_pawn,[1,4])"
gui_game = graphic_interface.App(game.pieces)

color_to_play = 'w'

while len(game.possible_moves(color_to_play))!=0:
    move = gui_game.on_execute(color_to_play)
    start_pos, fin_pos = move[0],move[1]
    print(start_pos,fin_pos)
    piece = game.get_piece_from_position([start_pos[0],start_pos[1]])

    if piece==0:
        print('No piece here')
        pass

    elif piece.color != color_to_play:
        print(f"{'white' if color_to_play=='w' else 'black'} to play")
        pass
    else:
        if game.move(piece, [fin_pos[0],fin_pos[1]])==0:
            gui_game.pieces = game.pieces
            gui_game.get_pieces(color_to_play)
            print('not a valid move')
            pass

        else:

            gui_game.pieces = game.pieces
            gui_game.get_pieces(color_to_play)

            if color_to_play =='w':
                color_to_play = 'b'

            else:
                color_to_play = 'w'

gui_game.on_cleanup()
