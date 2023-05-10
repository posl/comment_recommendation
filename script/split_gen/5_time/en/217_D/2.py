def main():
    L, Q = map(int, input().split())
    cuts = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            for j in range(len(cuts)):
                if cuts[j] == x:
                    print(cuts[j+1] - cuts[j-1])
                    break
