def main():
    import itertools
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    h = [h1, h2, h3]
    w = [w1, w2, w3]
    ans = 0
    for p in itertools.permutations(range(1, 31), 9):
        if p[0] + p[1] + p[2] == h[0] and p[3] + p[4] + p[5] == h[1] and p[6] + p[7] + p[8] == h[2] and p[0] + p[3] + p[6] == w[0] and p[1] + p[4] + p[7] == w[1] and p[2] + p[5] + p[8] == w[2]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()