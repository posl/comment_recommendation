def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                count += 1
    #print(count)
    if count == h + w - 1:
        print(1)
    else:
        print(2)
