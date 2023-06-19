def solve(A, B, C, D):
    if A >= B * D:
        return -1
    else:
        count = 0
        while A > C * D:
            A += B
            A -= C
            count += 1
        return count

if __name__ == '__main__':
    solve()