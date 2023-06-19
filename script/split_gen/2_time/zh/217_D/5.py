def main():
    L, Q = map(int, input().split())
    mark = [0] * (Q + 1)
    mark[0] = L
    mark[Q] = 0
    for i in range(1, Q + 1):
        c, x = map(int, input().split())
        if c == 1:
            mark[i] = x
        else:
            mark[i] = mark[x]
            print(mark[x] - mark[i - 1])
