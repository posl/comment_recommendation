def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    K = int(input())
    C = [0] * K
    D = [0] * K
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    
    ans = 0
    for i in range(2**K):
        tmp = 0
        ball = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                ball[C[j] - 1] += 1
            else:
                ball[D[j] - 1] += 1
        for j in range(M):
            if ball[A[j] - 1] > 0 and ball[B[j] - 1] > 0:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()