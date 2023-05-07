def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for a in range(1, 30):
        for b in range(1, 30):
            for c in range(1, 30):
                for d in range(1, 30):
                    for e in range(1, 30):
                        for f in range(1, 30):
                            for g in range(1, 30):
                                for i in range(1, 30):
                                    for j in range(1, 30):
                                        if h1 == a + b + c:
                                            if h2 == d + e + f:
                                                if h3 == g + i + j:
                                                    if w1 == a + d + g:
                                                        if w2 == b + e + i:
                                                            if w3 == c + f + j:
                                                                ans += 1
    print(ans)

if __name__ == '__main__':
    main()