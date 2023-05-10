def solve(A,B,C,D):
    if A <= B * D:
        return -1
    else:
        return (A + B - C - 1) // (B - C)

if __name__ == '__main__':
    solve()