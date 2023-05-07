def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for j in range(w):
        print(*[a[i][j] for i in range(h)])
