def solve():
    N = int(input())
    C = input()
    R = C.count('R')
    W = C.count('W')
    if R == 0 or W == 0:
        print(0)
        return
    r = 0
    w = 0
    for i in range(N):
        if C[i] == 'R':
            r += 1
        else:
            w += 1
        if r >= R or w >= W:
            print(i+1)
            return

if __name__ == '__main__':
    solve()