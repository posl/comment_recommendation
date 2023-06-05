def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for i in range(len(cut)):
                if cut[i] == x:
                    print(cut[i + 1] - cut[i - 1])
                    break
