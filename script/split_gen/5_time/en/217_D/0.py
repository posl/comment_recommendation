def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            n = len(cuts)
            for i in range(n):
                if cuts[i] == x:
                    print(cuts[i + 1] - cuts[i - 1])
                    break
