def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K - Q] * N
    for i in A:
        score[i - 1] += 1
    for i in score:
        if i > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()