def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            print(cut[cut.index(x) + 1] - cut[cut.index(x) - 1])
