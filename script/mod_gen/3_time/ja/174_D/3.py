def main():
    N = int(input())
    s = input()
    ans = 0
    r = 0
    for i in range(N):
        if s[i] == 'R':
            r += 1
        else:
            ans += r
    print(ans)

if __name__ == '__main__':
    main()