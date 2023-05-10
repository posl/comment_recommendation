def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans -= A[i]
    ans = abs(ans)
    ans = min(ans, 360 - ans)
    print(ans)
    return

if __name__ == '__main__':
    main()