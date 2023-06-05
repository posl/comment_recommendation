def main():
    N = int(input())
    c = input()
    r, w = 0, 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
    ans = 0
    for i in range(r):
        if c[i] == 'W':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()