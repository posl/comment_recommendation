def main():
    h,w = map(int,input().split())
    s = [list(input()) for i in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans += 1
    return ans
