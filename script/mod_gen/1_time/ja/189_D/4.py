def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2**n):
        y = i % 2
        for j in range(n):
            x = (i >> j) % 2
            if s[j] == 'AND':
                y = y & x
            else:
                y = y | x
        if y == 1:
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()