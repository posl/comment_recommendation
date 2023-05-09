def solve(h1, h2, h3, w1, w2, w3):
    s = set()
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if i + j + k == h1 and i + k + j == h2 and j + k + i == h3 and i + j + k == w1 and i + k + j == w2 and j + k + i == w3:
                    s.add((i, j, k))
    return len(s)
