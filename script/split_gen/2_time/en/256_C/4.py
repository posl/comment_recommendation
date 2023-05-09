def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for x1 in range(1, h1):
        for x2 in range(1, h2):
            for x3 in range(1, h3):
                for y1 in range(1, w1):
                    for y2 in range(1, w2):
                        for y3 in range(1, w3):
                            if (x1+x2+x3 == h1 and x1+x2+x3 == h2 and x1+x2+x3 == h3 and
                                y1+y2+y3 == w1 and y1+y2+y3 == w2 and y1+y2+y3 == w3 and
                                x1+y1 == x2+y2 == x3+y3):
                                ans += 1
    print(ans)
