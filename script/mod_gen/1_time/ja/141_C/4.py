def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K] * N
    for a in A:
        scores[a - 1] += 1
    for score in scores:
        if score - Q > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()