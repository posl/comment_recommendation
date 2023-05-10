def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s = [sorted(row) for row in s]
    t = [sorted(row) for row in t]
    s = sorted(s)
    t = sorted(t)
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print("No")
                return
    print("Yes")
    return
