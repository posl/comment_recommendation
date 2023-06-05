def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
    K = int(input())
    C = []
    D = []
    for _ in range(K):
        c, d = map(int, input().split())
        C.append(c-1)
        D.append(d-1)
    ans = 0
    for i in range(2 ** K):
        dish = [0] * N
        for j in range(K):
            if i >> j & 1:
                dish[C[j]] += 1
            else:
                dish[D[j]] += 1
        cnt = 0
        for j in range(M):
            if dish[A[j]] > 0 and dish[B[j]] > 0:
                cnt += 1
        if ans < cnt:
            ans = cnt
    print(ans)

if __name__ == '__main__':
    main()