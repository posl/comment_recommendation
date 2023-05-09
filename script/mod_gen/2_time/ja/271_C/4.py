def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if ans + 1 < A[i]:
            break
        ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()