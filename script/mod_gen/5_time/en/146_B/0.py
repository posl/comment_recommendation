def main():
    N = int(input())
    S = input()
    ans = ''
    for s in S:
        if ord(s) + N > 90:
            ans += chr(ord(s) + N - 26)
        else:
            ans += chr(ord(s) + N)
    print(ans)

if __name__ == '__main__':
    main()