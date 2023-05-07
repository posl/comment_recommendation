def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N//2):
        sum += min(L, A[i])
    for i in range(N//2, N):
        sum += min(R, A[i])
    print(sum)

if __name__ == '__main__':
    main()