def main():
    h, w, x, y = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    count = 0
    for i in range(x-1, -1, -1):
        if s[i][y-1] == '.':
            count += 1
        else:
            break
    for i in range(x, h):
        if s[i][y-1] == '.':
            count += 1
        else:
            break
    for i in range(y-2, -1, -1):
        if s[x-1][i] == '.':
            count += 1
        else:
            break
    for i in range(y, w):
        if s[x-1][i] == '.':
            count += 1
        else:
            break
    print(count)
