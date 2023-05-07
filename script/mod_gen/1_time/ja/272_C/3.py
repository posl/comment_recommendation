def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(N-1):
        if A[i] % 2 == 0:
            print(A[i])
            return
    print(-1)

if __name__ == '__main__':
    main()