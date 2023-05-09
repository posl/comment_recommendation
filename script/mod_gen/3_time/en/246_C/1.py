def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for a in A:
        if K > 0:
            if a > X:
                ans += X
                K -= 1
            else:
                ans += a
        else:
            ans += a
    print(ans)

if __name__ == '__main__':
    main()