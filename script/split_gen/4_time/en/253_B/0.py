def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                cnt += 1
    if cnt == 1:
        print(1)
    else:
        print(2)
main()
