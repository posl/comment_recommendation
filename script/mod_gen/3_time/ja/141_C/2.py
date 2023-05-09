def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    point = [K-Q] * N
    for a in A:
        point[a-1] += 1
    for p in point:
        if p > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()