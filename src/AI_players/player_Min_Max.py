from src.game.board import Board
import random

class Node:
    def __init__(self,name, age = (), parent= None):
        self.name = name
        self.age = age
        self.parent = parent
        self.children = []
        if parent != None:
            parent.children.append(self)

    def get_leaves(self, node,leaves):
            if node.children == []:
                leaves.append(node)
            else:
                for children in node.children:
                    self.get_leaves(children,leaves)

    def leaves(self):
        leaves = []
        self.get_leaves(self,leaves)
        return leaves
    # def delete_branch(self,leaf):



def evaluate_pos_simplest(board):
    """returns score for the position only based on pieces value"""
    piece_value = {'Q': 9, 'r': 5, 'b': 3, 'k': 3, 'p': 1, 'K':0}
    if board.result == 'w':
        return 250
    elif board.result == 'b':
        return -250
    elif board.result == 'd':
        return 0
    else:
        score = 0
        for piece in board.pieces['w']:
            score += piece_value[piece.piece_type]
        for piece in board.pieces['b']:
            score -= piece_value[piece.piece_type]
        return score

class Player_Min_Max:
    def __init__(self,color,board,depth):
        self.color = color
        self.board = board
        self.depth = depth

    def move(self):
        actual_depth = 0
        actual_score = evaluate_pos_simplest(self.board)
        color_to_play = self.color
        entire_pos = self.board.get_entire_position()
        root = Node("root", age=(actual_score, entire_pos, 0, 0))

        node_number = 0
        while actual_depth < self.depth:
            for leaf in root.leaves():
                score, entire_pos, pos_piece, move = leaf.age
                board_to_test = Board(0,entire_pos,moves=[],color_to_play=color_to_play)
                best_score, best_score_moves = self.best_moves(color_to_play,board_to_test)

                for pos_piece, move in best_score_moves:
                    board_to_test = Board(0,entire_pos,moves=[],color_to_play=color_to_play)
                    piece_to_move = board_to_test.get_piece_from_position(pos_piece)
                    board_to_test.Move(piece_to_move,move)
                    entire_pos_to_test = board_to_test.get_entire_position()

                    Node(f"{node_number}", age = (best_score,entire_pos_to_test,pos_piece,move), parent = leaf)
                    node_number +=1
            color_to_play = self.board.inverse_color(color_to_play)
            actual_depth += 1

        best_score = None
        best_moves_leaves = []
        for leaf in root.leaves():
            score, entire_pos, pos_piece, move = leaf.age
            if best_score is None:
                best_score = score
            if self.color == 'w':
                if score > best_score:
                    best_score = score
                    best_moves_leaves = [leaf]
                elif score == best_score:
                    best_moves_leaves.append(leaf)
                else:
                    pass
            else:
                if score < best_score:
                    best_score = score
                    best_moves_leaves = [leaf]
                elif score == best_score:
                    best_moves_leaves.append(leaf)
                else:
                    pass
        print(best_moves_leaves)
        random_leaf = best_moves_leaves[random.randint(0, len(best_moves_leaves) - 1)]
        leaf = random_leaf
        while leaf.parent.name != 'root':
            leaf = leaf.parent
        score, entire_pos, pos_piece, move = leaf.age
        piece_to_move = self.board.get_piece_from_position(pos_piece)
        self.board.Move(piece_to_move,move)


    @staticmethod
    def best_moves(color,board):
        best_score_moves = []
        best_score = evaluate_pos_simplest(board)
        if board.result == 'w':
            return 250, []
        elif board.result == 'b':
            return -250,[]
        elif board.result == 'd':
            return 0,[]
        else:
            for piece,move in board.possible_moves(color):
                position_to_test = board.get_entire_position()
                Position_to_test = Board(0,position_to_test,moves=[],color_to_play=color)
                piece_pos_to_test = Position_to_test.get_piece_from_position([piece.file, piece.row])
                Position_to_test.Move(piece_pos_to_test,move)
                score_pos_test = evaluate_pos_simplest(Position_to_test)
                Position_to_test.delete_all_pieces()
                del Position_to_test
                if color == 'w':
                    if score_pos_test > best_score:
                        best_score = score_pos_test
                        piece_pos = [piece.file, piece.row]
                        best_score_moves = [[piece_pos, move]]
                    elif score_pos_test == best_score:
                        piece_pos = [piece.file, piece.row]
                        best_score_moves.append([piece_pos, move])
                    else:
                        pass
                else:
                    if score_pos_test < best_score:
                        best_score = score_pos_test
                        piece_pos = [piece.file, piece.row]
                        best_score_moves = [[piece_pos, move]]
                    elif score_pos_test == best_score:
                        piece_pos = [piece.file, piece.row]
                        best_score_moves.append([piece_pos, move])
                    else:
                        pass
            return best_score,best_score_moves
