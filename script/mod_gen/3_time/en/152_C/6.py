def solve():
    N = int(input())
    P = list(map(int, input().split()))
    min = N+1
    count = 0
    for i in range(N):
        if min > P[i]:
            min = P[i]
            count += 1
    print(count)

if __name__ == '__main__':
    solve()