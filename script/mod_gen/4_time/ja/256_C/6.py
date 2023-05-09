def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i in range(1, 100):
        if (h1 + h2 + h3) % i != 0:
            continue
        for j in range(1, 100):
            if (w1 + w2 + w3) % j != 0:
                continue
            if (h1 + h2 + h3) // i != (w1 + w2 + w3) // j:
                continue
            if i * j <= h1 + h2 + h3:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()