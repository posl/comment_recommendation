def main():
    S = input()
    K = int(input())
    n = len(S)
    l = 0
    r = 0
    ans = 0
    while l < n:
        while r < n and S[r] == 'X':
            r += 1
        ans = max(ans, r - l)
        if K > 0:
            K -= 1
            r += 1
        l += 1
    print(ans)

if __name__ == '__main__':
    main()