def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    c = 0
    for a in range(1, h1):
        for b in range(1, h2):
            for c in range(1, h3):
                for d in range(1, w1):
                    for e in range(1, w2):
                        for f in range(1, w3):
                            if a + b + c == h1 and d + e + f == w1 and a + d == h2 and b + e == h3 and c + f == w2 and a + e + f == w3:
                                c += 1
    print(c)
