def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K - Q for _ in range(N)]
    for i in range(Q):
        score[A[i] - 1] += 1
    for i in score:
        if i <= 0:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()