def solve(h1,h2,h3,w1,w2,w3):
    if sum([h1,h2,h3]) != sum([w1,w2,w3]):
        return 0
    else:
        return 1

if __name__ == '__main__':
    solve()