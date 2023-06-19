def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        for j in range(i+1, N):
            if (A[i]+A[j])%2 == 0:
                print(A[i]+A[j])
                return
    print(-1)

if __name__ == '__main__':
    main()