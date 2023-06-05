def solve(h1,h2,h3,w1,w2,w3):
    result = 0
    for a1 in range(1,31):
        for a2 in range(1,31):
            for a3 in range(1,31):
                for a4 in range(1,31):
                    for a5 in range(1,31):
                        for a6 in range(1,31):
                            if a1+a2+a3 == h1 and a4+a5+a6 == h2 and a1+a4 == w1 and a2+a5 == w2 and a3+a6 == w3:
                                result += 1
    return result
h1,h2,h3,w1,w2,w3 = map(int,input().split())
print(solve(h1,h2,h3,w1,w2,w3))
