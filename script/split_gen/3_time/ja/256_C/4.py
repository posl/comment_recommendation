def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i in range(1, h1 + 1):
        for j in range(1, h2 + 1):
            for k in range(1, h3 + 1):
                for l in range(1, w1 + 1):
                    for m in range(1, w2 + 1):
                        for n in range(1, w3 + 1):
                            if i + j + k == h1 and i + l + m == w1 and j + m + n == w2 and k + l + n == w3:
                                ans += 1
    print(ans)
