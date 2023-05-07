def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i1 in range(1, h1):
        for i2 in range(1, h2):
            for i3 in range(1, h3):
                for j1 in range(1, w1):
                    for j2 in range(1, w2):
                        for j3 in range(1, w3):
                            if i1 + i2 + i3 == h1 and i1 + j1 + j2 + j3 == w1 and i2 + j1 + j2 == w2 and i3 + j1 + j3 == w3 and i1 + i2 + j1 == h2 and i2 + i3 + j2 == h3 and i1 + j1 + j3 == h3 and i3 + j2 + j3 == h3:
                                ans += 1
    print(ans)
