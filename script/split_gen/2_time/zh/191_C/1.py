def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            if s[i][j] == '#':
                ans += 1
                s[i][j],s[i][j+1],s[i+1][j],s[i+1][j+1] = '.','.','.','.'
    print(ans)
