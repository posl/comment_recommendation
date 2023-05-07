def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    l = 0
    r = M + 1
    while r - l > 1:
        c = (l + r) // 2
        if d ** len(X) < M:
            l = c
        else:
            r = c
    print(r - d)
