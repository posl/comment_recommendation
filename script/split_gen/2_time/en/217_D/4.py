def main():
    l, q = map(int, input().split())
    cuts = [0, l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            i = cuts.index(x)
            print(cuts[i] - cuts[i-1])
