def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.reverse()
    ans = 0
    for i in range(N-1):
        if A[i] <= A[i+1]:
            ans += A[i+1] - A[i]
        else:
            ans += A[i+1]
    print(ans)

if __name__ == '__main__':
    main()