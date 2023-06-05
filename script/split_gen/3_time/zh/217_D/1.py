def main():
    l, q = map(int, input().split())
    cut = [0] * q
    for i in range(q):
        cut[i] = list(map(int, input().split()))
    cut.sort(key=lambda x: x[1])
    mark = []
    for i in range(q):
        if cut[i][0] == 1:
            mark.append(cut[i][1])
        else:
            mark.remove(cut[i][1])
            if i == q - 1:
                print(l - mark[0])
            else:
                print(cut[i + 1][1] - cut[i - 1][1])
