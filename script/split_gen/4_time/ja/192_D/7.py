def main():
    X = int(input())
    M = int(input())
    d = max(list(map(int, list(str(X)))))
    if X <= M:
        print(1)
        return
    l = d + 1
    r = 10 ** 18 + 1
    while r - l > 1:
        m = (l + r) // 2
        x = 0
        for i, c in enumerate(str(X)):
            x += int(c) * (m ** (len(str(X)) - i - 1))
            if x > M:
                break
        if x <= M:
            l = m
        else:
            r = m
    print(l - d)
