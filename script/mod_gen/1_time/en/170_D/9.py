def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] == 1:
        print(0)
        return
    ans = A.count(A[0])
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans += A.count(A[i])
    print(ans)

if __name__ == '__main__':
    main()