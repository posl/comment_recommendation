def main():
    N, M = map(int, input().split())
    # 連結リスト
    connect = {i:[] for i in range(1, N+1)}
    for i in range(M):
        A, B = map(int, input().split())
        connect[A].append(B)
        connect[B].append(A)
    for i in range(1, N+1):
        connect[i].sort()
        print(len(connect[i]), *connect[i])
