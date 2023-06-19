def solve(a,b,c,d):
    if a < b:
        return -1
    else:
        if d * c - b > 0:
            return int((a - b) / (d * c - b)) + 1
        else:
            return -1

if __name__ == '__main__':
    solve()