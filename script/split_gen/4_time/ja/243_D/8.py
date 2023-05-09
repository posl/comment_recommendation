def calc_next_pos(pos, move):
    if move == "U":
        return pos // 2
    elif move == "L":
        return pos * 2
    elif move == "R":
        return pos * 2 + 1
    else:
        assert False
