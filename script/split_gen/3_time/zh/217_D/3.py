def main():
    L, Q = map(int, input().split())
    mark = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark.append(x)
        else:
            mark.sort()
            index = mark.index(x)
            print(mark[index] - mark[index - 1])
    return
