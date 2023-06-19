def solve():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort()
    ans = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()