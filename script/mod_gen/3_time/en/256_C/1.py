def solve(h1,h2,h3,w1,w2,w3):
    count = 0
    for a in range(1,31):
        for b in range(1,31):
            for c in range(1,31):
                for d in range(1,31):
                    for e in range(1,31):
                        for f in range(1,31):
                            for g in range(1,31):
                                for i in range(1,31):
                                    for j in range(1,31):
                                        if a+b+c == h1 and d+e+f == h2 and g+i+j == h3 and a+d+g == w1 and b+e+i == w2 and c+f+j == w3:
                                            count += 1
    return count
h1,h2,h3,w1,w2,w3 = map(int,input().split())
print(solve(h1,h2,h3,w1,w2,w3))
