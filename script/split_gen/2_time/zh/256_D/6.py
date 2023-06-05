def solve(h1, h2, h3, w1, w2, w3):
    from itertools import permutations
    count = 0
    for p in permutations(range(1, 10)):
        if p[0] + p[1] + p[2] == h1 and p[3] + p[4] + p[5] == h2 and p[6] + p[7] + p[8] == h3:
            if p[0] + p[3] + p[6] == w1 and p[1] + p[4] + p[7] == w2 and p[2] + p[5] + p[8] == w3:
                count += 1
    return count
h1, h2, h3, w1, w2, w3 = map(int, input().split())
print(solve(h1, h2, h3, w1, w2, w3))
