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
                                        if a + b + c == h1 and d + e + f == h2 and g + i + j == h3 and a + d + g == w1 and b + e + i == w2 and c + f + j == w3:
                                            ans += 1
    print(ans)
