def main():
    N = int(input())
    ans = 0
    if N < 1000:
        ans = 0
    elif N < 1000000:
        ans = N - 999
    elif N < 1000000000:
        ans = 1000000 - 1000 + (N - 999999) * 2
    elif N < 1000000000000:
        ans = 1000000000 - 1000000 + 1999000 + (N - 999999999) * 3
    elif N < 1000000000000000:
        ans = 1000000000000 - 1000000000 + 2999000000 + (N - 999999999999) * 4
    else:
        ans = 1000000000000000 - 1000000000000 + 3999000000000 + (N - 999999999999999) * 5
    print(ans)

if __name__ == '__main__':
    main()