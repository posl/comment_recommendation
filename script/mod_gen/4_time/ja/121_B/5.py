def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for a in A:
        sum = 0
        for i in range(M):
            sum += a[i] * B[i]
        sum += C
        if sum > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()