def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    h = [h1, h2, h3]
    w = [w1, w2, w3]
    ans = 0
    for i in range(1, 30):
        for j in range(1, 30):
            for k in range(1, 30):
                if h[0] == i + j + k and w[0] == i + w[1] + w[2]:
                    if h[1] == i + w[1] + k and w[1] == j + w[2] + k:
                        if h[2] == i + j + w[2] and w[2] == j + w[1] + k:
                            ans += 1
    print(ans)
