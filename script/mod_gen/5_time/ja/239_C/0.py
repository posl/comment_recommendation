def solve(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return False
    elif x1 == x2 and y1 != y2:
        return True
    elif x1 != x2 and y1 == y2:
        return True
    else:
        return abs(x1 - x2) == abs(y1 - y2)

if __name__ == '__main__':
    solve()