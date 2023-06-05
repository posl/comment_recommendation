def solution(x, y):
    if 0 <= y <= 2:
        return x + "-"
    elif 3 <= y <= 6:
        return x
    else:
        return x + "+"
