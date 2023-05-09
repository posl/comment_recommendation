def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                ans += 1
    print(ans)
