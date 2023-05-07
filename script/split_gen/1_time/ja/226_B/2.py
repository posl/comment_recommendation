def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    for i in range(N):
        L[i][0] = int(L[i][0])
        for j in range(1,L[i][0]+1):
            L[i][j] = int(L[i][j])
    L.sort()
    ans = 1
    for i in range(1,N):
        if L[i-1][0] != L[i][0]:
            ans += 1
        else:
            for j in range(1,L[i][0]+1):
                if L[i-1][j] != L[i][j]:
                    ans += 1
                    break
    print(ans)
