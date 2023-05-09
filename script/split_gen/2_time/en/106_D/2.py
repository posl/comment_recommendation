def main():
    N, M, Q = map(int, input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0]*Q
    q = [0]*Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    for i in range(Q):
        cnt = 0
        for j in range(M):
            if L[j] >= p[i] and R[j] <= q[i]:
                cnt += 1
        print(cnt)
