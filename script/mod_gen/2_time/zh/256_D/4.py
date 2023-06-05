def solve(h,w):
    h1 = h[0]
    h2 = h[1]
    h3 = h[2]
    w1 = w[0]
    w2 = w[1]
    w3 = w[2]
    if (h1+h2+h3 != w1+w2+w3):
        return 0
    if (h1+h2+h3 != sum([w1,w2,w3])):
        return 0
    if (h1+h2+h3 != sum([h1,h2,h3])):
        return 0
    if (h1+h2+h3 != sum([w1+w2+w3])):
        return 0
    if (h1+h2+h3 != sum([w1+w2+w3])):
        return 0
    if (h1+h2+h3 != sum([h1+h2+h3])):
        return 0
    if (h1+h2+h3 != sum([h1+h2+h3])):
        return 0
    if (h1+h2+h3 != sum([h1+h2+h3])):
        return 0
    if (h1+h2+h3 != sum([h1+h2+h3])):
        return 0
    if (h1+h2+h3 != sum([h1+h2+h3])):
        return 0
    if (h1+h2+h3 != sum([h1+h2+h3])):
        return 0
    if (h1+h2+h3 != sum([h1+h2+h3])):
        return 0
    return 1

if __name__ == '__main__':
    solve()