def main():
    import math
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    #print(N, X, L)
    ans = 0
    for i in range(N):
        for j in range(1, L[i][0]+1):
            if X % L[i][j] == 0:
                ans += 1
    print(ans)
