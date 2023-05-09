def main():
    N = input()
    ans = 0
    for i in range(1, len(N)):
        a = N[:i]
        b = N[i:]
        ans = max(ans, int(a) * int(b))
    print(ans)

if __name__ == '__main__':
    main()