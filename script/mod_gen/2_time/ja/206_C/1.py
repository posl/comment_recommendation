def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += N - i - 1
    print(ans)

if __name__ == '__main__':
    main()