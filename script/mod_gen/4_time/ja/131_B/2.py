def solve():
    N, L = map(int, input().split())
    sum = 0
    min = 1000
    for i in range(N):
        sum += L + i
        if min > abs(L + i):
            min = abs(L + i)
    print(sum - min)

if __name__ == '__main__':
    solve()