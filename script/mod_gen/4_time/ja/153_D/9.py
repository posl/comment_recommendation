def solve(H):
    if H == 1:
        return 1
    else:
        return 1 + 2*solve(H // 2)

if __name__ == '__main__':
    solve()