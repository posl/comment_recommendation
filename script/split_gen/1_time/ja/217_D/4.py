def main():
    l, q = map(int, input().split())
    cut = [0] * (q + 1)
    for i in range(1, q + 1):
        c, x = map(int, input().split())
        if c == 1:
            cut[i] = x
    cut = sorted(cut)
    cut.append(l)
    for i in range(1, q + 1):
        cut[i] += cut[i - 1]
    for i in range(1, q + 1):
        print(cut[i] - cut[i - 1])
