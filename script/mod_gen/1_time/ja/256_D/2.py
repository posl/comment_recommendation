def solve():
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    # 1つの区間に収まる
    if L[N-1] == R[0]:
        print(L[N-1], R[0])
    # 2つの区間に分かれる
    else:
        print(L[0], R[N-1])

if __name__ == '__main__':
    solve()