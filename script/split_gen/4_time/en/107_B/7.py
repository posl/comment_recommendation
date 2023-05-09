def main():
    h, w = map(int, input().split())
    a = [input() for i in range(h)]
    b = []
    for i in range(h):
        if not all(j == "." for j in a[i]):
            b.append(a[i])
    c = []
    for i in range(w):
        if not all(j == "." for j in [a[j][i] for j in range(h)]):
            c.append([a[j][i] for j in range(h)])
    for i in range(len(b)):
        print("".join(b[i]))
    print()
