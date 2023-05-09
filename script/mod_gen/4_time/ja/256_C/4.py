def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    ans += h1 * w1
    ans += h2 * w2
    ans += h3 * w3
    print(ans)

if __name__ == '__main__':
    main()