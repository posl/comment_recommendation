def can_jump(x, jump):
    if x == 0:
        return True
    if jump == []:
        return False
    return can_jump(x-jump[0], jump[1:]) or can_jump(x+jump[0], jump[1:])
