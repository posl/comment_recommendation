def solve(H, A):
    num = 0
    while H > 0:
        H -= A
        num += 1
    return num

if __name__ == '__main__':
    solve()