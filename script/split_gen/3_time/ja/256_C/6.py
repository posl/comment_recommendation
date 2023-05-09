def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for h4 in range(1, 31):
        for h5 in range(1, 31):
            for h6 in range(1, 31):
                for w4 in range(1, 31):
                    for w5 in range(1, 31):
                        for w6 in range(1, 31):
                            if h1 == h4 + h5 + h6 and h2 == h4 + h5 + h6 and h3 == h4 + h5 + h6:
                                if w1 == w4 + w5 + w6 and w2 == w4 + w5 + w6 and w3 == w4 + w5 + w6:
                                    ans += 1
    print(ans)
