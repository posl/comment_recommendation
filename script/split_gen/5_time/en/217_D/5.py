def main():
    L, Q = map(int, input().split())
    cuts = []
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            for j in range(len(cuts)):
                if cuts[j] > x:
                    break
            if j == 0:
                print(cuts[j])
            elif j == len(cuts):
                print(L - cuts[j - 1])
            else:
                print(cuts[j] - cuts[j - 1])
