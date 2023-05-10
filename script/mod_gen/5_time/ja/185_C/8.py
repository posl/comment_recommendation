def main():
    l = int(input())
    ans = 0
    for i in range(1, l - 10):
        ans += comb(l - i - 11, i)
    print(ans)

if __name__ == '__main__':
    main()