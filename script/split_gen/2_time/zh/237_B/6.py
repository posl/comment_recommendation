def main():
    h, w = [int(i) for i in input().split()]
    a = []
    for _ in range(h):
        a.append([int(i) for i in input().split()])
    for i in range(w):
        for j in range(h):
            print(a[j][i], end=' ')
        print()
