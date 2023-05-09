def main():
    h,w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                cnt += 1
    print(cnt)
