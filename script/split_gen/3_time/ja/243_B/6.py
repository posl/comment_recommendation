def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] * N
    D = [0] * N
    for i in range(N):
        C[A[i] - 1] = i
        D[B[i] - 1] = i
    cnt = 0
    for i in range(N):
        if C[i] == D[i]:
            cnt += 1
    print(cnt)
    cnt = 0
    for i in range(N):
        if C[i] != D[i]:
            for j in range(i + 1, N):
                if C[i] == D[j] and C[j] == D[i]:
                    cnt += 1
    print(cnt)
