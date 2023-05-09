def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                ans += 1
    if ans == 1:
        print(1)
    else:
        print(0)
