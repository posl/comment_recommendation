def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                count += 1
    if count == 1:
        print(1)
    else:
        print(2)
