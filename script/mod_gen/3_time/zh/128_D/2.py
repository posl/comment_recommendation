def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    # print(N, K, V)
    max_sum = 0
    for i in range(K+1):
        for j in range(K+1-i):
            if i+j > N:
                continue
            # print(i, j, N-i-j)
            # print(V[:i])
            # print(V[N-j:])
            sum = 0
            if i > 0:
                sum += sum(V[:i])
            if j > 0:
                sum += sum(V[N-j:])
            if sum > max_sum:
                max_sum = sum
    print(max_sum)

if __name__ == '__main__':
    main()