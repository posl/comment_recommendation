def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for a in range(1, 31):
        for b in range(1, 31):
            for c in range(1, 31):
                for d in range(1, 31):
                    for e in range(1, 31):
                        for f in range(1, 31):
                            for g in range(1, 31):
                                for i in range(1, 31):
                                    for j in range(1, 31):
                                        if h1 == a + b + c and h2 == d + e + f and h3 == g + i + j and w1 == a + d + g and w2 == b + e + i and w3 == c + f + j:
                                            ans += 1
    print(ans)

if __name__ == '__main__':
    main()