def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] > ans + 1:
            break
        ans += A[i]
    print(ans + 1)

if __name__ == '__main__':
    main()