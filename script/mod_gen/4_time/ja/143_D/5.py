def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    solve()