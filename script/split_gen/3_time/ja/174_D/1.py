def main():
    N = int(input())
    C = input()
    R = C.count('R')
    W = C.count('W')
    if R == 0 or W == 0:
        print(0)
        exit()
    r = 0
    w = 0
    ans = 1000000000
    for i in range(N):
        if C[i] == 'R':
            r += 1
        else:
            w += 1
        ans = min(ans, r + W - w)
    print(ans)
