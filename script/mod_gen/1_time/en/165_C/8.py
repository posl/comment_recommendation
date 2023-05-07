def main():
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[N-1] = M
    score = [0]
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        score.append(d)
        A[a-1] = c + 1
        A[b-1] = M - c
    print(sum(score))

if __name__ == '__main__':
    main()