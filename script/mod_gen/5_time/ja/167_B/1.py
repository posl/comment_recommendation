def main():
    A, B, C, K = map(int, input().split())
    ans = 0
    if A >= K:
        ans = K
    else:
        ans = A
        K -= A
        if B >= K:
            pass
        else:
            K -= B
            ans -= K
    print(ans)

if __name__ == '__main__':
    main()