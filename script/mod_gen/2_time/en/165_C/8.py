def main():
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[N-1] = M
    print(A)
    # for i in range(Q):
    #     a, b, c, d = map(int, input().split())
    #     if A[b-1] - A[a-1] == c:
    #         score += d
    # print(score)

if __name__ == '__main__':
    main()