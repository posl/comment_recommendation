def main():
    L, Q = map(int, input().split())
    cut = [0] * (Q + 1)
    for i in range(1, Q + 1):
        c, x = map(int, input().split())
        if c == 1:
            cut[i] = x
    cut[0] = 0
    cut[Q] = L
    cut.sort()
    for i in range(1, Q + 1):
        if cut[i] == 0:
            continue
        print(cut[i] - cut[i - 1])
