def main():
    L, Q = map(int, input().split())
    #print(L, Q)
    cut = [0] * (L + 1)
    cut[0] = 1
    cut[L] = 1
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut[x] = 1
        if c == 2:
            #print(cut)
            for j in range(x, -1, -1):
                if cut[j] == 1:
                    x1 = j
                    break
            for j in range(x, L + 1):
                if cut[j] == 1:
                    x2 = j
                    break
            print(x2 - x1)
