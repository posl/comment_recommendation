def f(h1,h2,h3,w1,w2,w3):
    #h1,h2,h3,w1,w2,w3=map(int,input().split())
    #print(h1,h2,h3,w1,w2,w3)
    if h1+h2+h3!=w1+w2+w3:
        return 0
    if h1>h2:
        h1,h2=h2,h1
    if h2>h3:
        h2,h3=h3,h2
    if h1>h2:
        h1,h2=h2,h1
    if w1>w2:
        w1,w2=w2,w1
    if w2>w3:
        w2,w3=w3,w2
    if w1>w2:
        w1,w2=w2,w1
    #print(h1,h2,h3,w1,w2,w3)
    if h1<=w1 and h2<=w2 and h3<=w3:
        return 1
    if h1<=w1 and h2<=w2 and h3<=w1+w2:
        return 3
    if h1<=w1 and h2<=w2 and h3<=w2+w3:
        return 3
    if h1<=w1 and h2<=w2 and h3<=w1+w3:
        return 3
    if h1<=w1 and h2<=w2 and h3<=w1+w2+w3:
        return 6
    if h1<=w1 and h2<=w2+w3 and h3<=w2+w3:
        return 6
    if h1<=w1 and h2<=w2+w3 and h3<=w1+w2+w3:
        return 6
    if h1<=w1+w2 and h2<=w1+w2 and h3<=w1+w2+w3:
        return 6
    if h1<=w1+w2 and h2<=w1+w2+w3 and h3<=w1+w2+w3:
        return 6
    if h1<=w1+w2+w3 and h2<=w1+w2+w3 and h3<=w1+w2+w3:
        return 6
    if h1<=w1
