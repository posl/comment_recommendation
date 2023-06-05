def solve():
    L = int(input())
    N = 2 * L
    M = L + 1
    print(N, M)
    for i in range(1, L):
        print(i, i+1, 0)
        print(i, i+1, 1)
    print(L, L+1, 0)

if __name__ == '__main__':
    solve()