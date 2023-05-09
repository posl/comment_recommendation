def main():
    N, M = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(M):
        p, S = input().split()
        p = int(p) - 1
        if S == "AC":
            A[p] = 1
        else:
            if A[p] == 0:
                B[p] += 1
    ans = 0
    pen = 0
    for i in range(N):
        if A[i] == 1:
            ans += 1
            pen += B[i]
    print(ans, pen)

if __name__ == '__main__':
    main()