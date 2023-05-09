def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if h1 == i + j + k and w1 == i + j + k:
                    for l in range(1, 31):
                        for m in range(1, 31):
                            for n in range(1, 31):
                                if h2 == l + m + n and w2 == l + m + n:
                                    for o in range(1, 31):
                                        for p in range(1, 31):
                                            for q in range(1, 31):
                                                if h3 == o + p + q and w3 == o + p + q:
                                                    if i + l + o == j + m + p == k + n + q:
                                                        count += 1
    print(count)
