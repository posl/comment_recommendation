def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if "#" in a[i]:
            b.append(a[i])
    c = [list(x) for x in zip(*b)]
    d = []
    for i in range(w):
        if "#" in c[i]:
            d.append(c[i])
    e = [list(x) for x in zip(*d)]
    for i in range(len(e)):
        print("".join(e[i]))
