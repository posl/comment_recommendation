def solve(h1,h2,h3,w1,w2,w3):
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,10):
                    for m in range(1,10):
                        for n in range(1,10):
                            if i + j + k == h1 and l + m + n == h2 and i + l == w1 and j + m == w2 and k + n == w3 and i + j + k == h1 and l + m + n == h2 and i + l == w1 and j + m == w2 and k + n == w3:
                                ans += 1
    return ans
