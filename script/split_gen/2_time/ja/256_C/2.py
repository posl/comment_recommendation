def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if i + j + k == h1 and i + k + k == w1:
                    for l in range(1, 31):
                        for m in range(1, 31):
                            for n in range(1, 31):
                                if l + m + n == h2 and l + n + n == w2:
                                    for o in range(1, 31):
                                        for p in range(1, 31):
                                            for q in range(1, 31):
                                                if o + p + q == h3 and o + q + q == w3:
                                                    if i == l == o and j == m == p and k == n == q:
                                                        count += 1
    print(count)
