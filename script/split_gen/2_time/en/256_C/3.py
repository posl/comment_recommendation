def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    ans = 0
    for a in range(1,31):
        for b in range(1,31):
            for c in range(1,31):
                for d in range(1,31):
                    for e in range(1,31):
                        for f in range(1,31):
                            if a+b+c == h1 and d+e+f == h2 and a+d == w1 and b+e == w2 and c+f == w3 and c+e == h3:
                                ans += 1
    print(ans)
