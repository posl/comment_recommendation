def main():
    n, k, x = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(A[i]-x, 0)
            k -= 1
        else:
            ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()