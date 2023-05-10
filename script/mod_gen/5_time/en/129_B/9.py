def solve():
    N = int(input())
    W = list(map(int, input().split()))
    min = 100 * 100
    for t in range(1, N):
        S1 = sum(W[:t])
        S2 = sum(W[t:])
        diff = abs(S2 - S1)
        if diff < min:
            min = diff
    print(min)

if __name__ == '__main__':
    solve()