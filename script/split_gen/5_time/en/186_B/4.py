def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_a = min([min(a[i]) for i in range(h)])
    print(sum([sum([a[i][j] - min_a for j in range(w)]) for i in range(h)]))
