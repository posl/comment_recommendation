def main():
    l, q = map(int, input().split())
    cut = [0, l]
    for i in range(q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for j in range(len(cut)):
                if cut[j] == x:
                    print(cut[j+1] - cut[j-1])
                    cut.pop(j)
                    break
