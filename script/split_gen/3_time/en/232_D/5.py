def main():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    count = 1
    i = j = 0
    while i < h and j < w:
        if i == h - 1 and j == w - 1:
            break
        if i + 1 < h and c[i + 1][j] == '.':
            i += 1
        elif j + 1 < w and c[i][j + 1] == '.':
            j += 1
        else:
            break
        count += 1
    print(count)
