def main():
    l = int(input())
    ans = 0
    for i in range(1, l):
        for j in range(i, l):
            ans = max(ans, i * j * (l - i - j))
    print(ans)

if __name__ == '__main__':
    main()