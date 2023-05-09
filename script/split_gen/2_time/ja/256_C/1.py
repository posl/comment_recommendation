def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if h1 == i + j + k and w1 == i + w2 + w3 and w2 == j + w1 + w3 and w3 == k + w1 + w2 and h2 == i + w2 + k and h3 == j + w3 + k:
                    ans += 1
    print(ans)
