def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            t = 0
            for k in range(j-1,-1,-1):
                if s[i][k] == '#':
                    break
                t += 1
            for k in range(j+1,w):
                if s[i][k] == '#':
                    break
                t += 1
            for k in range(i-1,-1,-1):
                if s[k][j] == '#':
                    break
                t += 1
            for k in range(i+1,h):
                if s[k][j] == '#':
                    break
                t += 1
            ans = max(ans,t)
    print(ans+1)

if __name__ == '__main__':
    main()