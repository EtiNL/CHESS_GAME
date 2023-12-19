# Todo:

- allow black to promote V
- get a way to choose promotion (another window or comand line)
- code first move for king and rook and make sure the engine respect the rule V
- code a best player AI
- code a me looking AI
- code en passant V
- code draw by repetition
- code board.result = 0 (if not finished), 'w' (if white won), 'b' (if black won), 'd' (if draw)

# Debbug:

- change the way the game is rendered so it don't flicker
- block castling if the intermediary square is in the opposite color vision V
- 'not a valid move' on black king check by taking
- allow taking a piece that is checking the opposite king or just blocking (the engine probably only allow a king move if is_checked)
