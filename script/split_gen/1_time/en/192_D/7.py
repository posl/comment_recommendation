def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        print(1 if d <= M else 0)
        return
    x = int(X, d + 1)
    if x <= M:
        print(x - d)
        return
    l, r = d + 1, 10 ** 18
    while r - l > 1:
        m = (l + r) // 2
        if int(X, m) <= M:
            l = m
        else:
            r = m
    print(l - d)
