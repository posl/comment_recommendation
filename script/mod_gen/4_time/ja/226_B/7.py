def solve():
    N = int(input())
    L = []
    for _ in range(N):
        L.append([int(x) for x in input().split()])
    L.sort(key=lambda x: x[1:])
    ans = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()