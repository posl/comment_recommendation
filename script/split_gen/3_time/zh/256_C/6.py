def solve(h1,h2,h3,w1,w2,w3):
    ans = 0
    for a in range(1,10000):
        for b in range(1,10000):
            for c in range(1,10000):
                if a+b+c == h1 and a+b+c == h2 and a+b+c == h3 and a+b+c == w1 and a+b+c == w2 and a+b+c == w3:
                    ans += 1
    print(ans)
h1,h2,h3,w1,w2,w3 = map(int,input().split())
solve(h1,h2,h3,w1,w2,w3)
