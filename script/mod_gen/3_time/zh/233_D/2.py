def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        temp = 0
        for j in range(i, N):
            temp += A[j]
            if temp == K:
                count += 1
    print(count)

if __name__ == '__main__':
    main()