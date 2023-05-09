def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            for i, cut in enumerate(cuts):
                if cut == x:
                    print(cuts[i + 1] - cuts[i])
                    break
