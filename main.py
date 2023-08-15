from src.game import board
from src.graphic_interface import graphic_interface

game = board.Board(1,0)
"A_pawn = game.get_piece_from_position([1,2])"
"game.move(A_pawn,[1,4])"
gui_game = graphic_interface.App(game.pieces)

color_to_play = 'w'

while len(game.possible_moves(color_to_play))!=0:
    move = gui_game.on_execute()
    start_pos, fin_pos = move[0],move[1]
    print(start_pos,fin_pos)
    piece = game.get_piece_from_position([start_pos[0],start_pos[1]])
    if piece==0:
        print(start_pos,fin_pos)
        break

    if game.move(piece, [fin_pos[0],fin_pos[1]]):
        gui_game.pieces = game.pieces
        gui_game.get_pieces()
        print('not a valid move')
        continue

    gui_game.pieces = game.pieces
    gui_game.get_pieces()

    if color_to_play =='w':
        color_to_play = 'b'

    else:
        color_to_play = 'w'

gui_game.on_cleanup()
