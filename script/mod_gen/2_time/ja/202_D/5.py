def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 and B > 0:
        if A > B:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
    if A > 0:
        ans += "a" * A
    else:
        ans += "b" * B
    print(ans)

if __name__ == '__main__':
    main()