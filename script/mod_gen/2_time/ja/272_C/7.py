def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    ans = -1
    for i in range(N-1):
        if A[i] % 2 == 0:
            ans = max(ans, A[i]+A[i])
    print(ans)

if __name__ == '__main__':
    main()