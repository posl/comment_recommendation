def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for i in range(h):
        if a[i] == "." * w:
            a[i] = ""
    for j in range(w):
        if all(a[i][j] == "." for i in range(h)):
            for i in range(h):
                a[i] = a[i][:j] + a[i][j+1:]
    for i in range(h):
        print(a[i])
