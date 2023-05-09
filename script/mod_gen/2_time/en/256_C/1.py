def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for a in range(1, h1 + 1):
        for b in range(1, h2 + 1):
            for c in range(1, h3 + 1):
                for d in range(1, w1 + 1):
                    for e in range(1, w2 + 1):
                        for f in range(1, w3 + 1):
                            if a + b + c == h1 and a + d + e == w1 and b + d + f == w2 and c + e + f == w3:
                                ans += 1
    print(ans)

if __name__ == '__main__':
    main()