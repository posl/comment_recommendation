def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    C = [0 for _ in range(N)]
    for i in range(N):
        B[i] = i, A[i]
    B.sort(key=lambda x: x[1])
    for i in range(N):
        C[B[i][0]] = i
    cnt = K // N
    K = K % N
    for i in range(N):
        if K > 0:
            print(cnt + 1)
            K -= 1
        else:
            print(cnt)
    return
