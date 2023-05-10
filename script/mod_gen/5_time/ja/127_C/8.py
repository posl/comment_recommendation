def solve():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)

if __name__ == '__main__':
    solve()