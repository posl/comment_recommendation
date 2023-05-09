def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        s[i] = s[i] + s[i]
    for i in range(h):
        t[i] = t[i] + t[i]
    for i in range(h):
        for j in range(w):
            if s[i][j:j+w] == t[i]:
                break
        else:
            print("No")
            break
    else:
        print("Yes")
