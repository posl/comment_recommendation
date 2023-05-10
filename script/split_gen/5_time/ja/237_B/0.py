def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    for i in range(w):
        for j in range(h):
            print(a[j][i], end=" ")
        print()
