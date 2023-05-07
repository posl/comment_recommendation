def main():
    N, M = map(int, input().split())
    # 都市iと道路で直接結ばれた都市の数
    d = [0] * N
    # 都市iと道路で直接結ばれた都市の集合
    a = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        d[A-1] += 1
        d[B-1] += 1
        a[A-1].append(B)
        a[B-1].append(A)
    for i in range(N):
        print(d[i], *sorted(a[i]))
