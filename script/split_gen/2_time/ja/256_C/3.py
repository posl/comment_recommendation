def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    #print(h1, h2, h3, w1, w2, w3)
    c = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if h1 == i + j + k and h2 == i + j + k and h3 == i + j + k and w1 == i + i + i and w2 == j + j + j and w3 == k + k + k:
                    c += 1
    print(c)
