def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [x - 1 for x in A]
    share = [0] * N
    share[X - 1] = 1
    for i in range(N):
        share[A[i]] += share[i]
    print(sum(share))

if __name__ == '__main__':
    main()