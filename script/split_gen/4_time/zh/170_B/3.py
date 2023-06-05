def solve(x,y):
    for i in range(x+1):
        j = x - i
        if 2*i + 4*j == y:
            return True
    return False
