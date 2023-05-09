def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 and B > 0:
        # aを先頭にする場合の数
        cnt = comb(A + B - 1, A - 1)
        if cnt >= K:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
            K -= cnt
    ans += "a" * A
    ans += "b" * B
    print(ans)

if __name__ == '__main__':
    main()