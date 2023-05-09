def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    cnt = 0
    for i in range(N+1):
        for j in range(i+1, N+1):
            if A[j]-A[i] == K:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()