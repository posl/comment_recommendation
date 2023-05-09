def solve():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if H[i] >= max:
            max = H[i]
    print(max)

if __name__ == '__main__':
    solve()