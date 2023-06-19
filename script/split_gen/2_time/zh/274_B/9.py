def main():
    h,w = map(int,input().split())
    c = [input() for _ in range(h)]
    ans = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                ans[i][j] = '#'
    for i in range(h):
        for j in range(w):
            if ans[i][j] == '#':
                if i-1 >= 0:
                    if ans[i-1][j] != '#':
                        ans[i-1][j] += 1
                if i+1 < h:
                    if ans[i+1][j] != '#':
                        ans[i+1][j] += 1
                if j-1 >= 0:
                    if ans[i][j-1] != '#':
                        ans[i][j-1] += 1
                if j+1 < w:
                    if ans[i][j+1] != '#':
                        ans[i][j+1] += 1
                if i-1 >= 0 and j-1 >= 0:
                    if ans[i-1][j-1] != '#':
                        ans[i-1][j-1] += 1
                if i-1 >= 0 and j+1 < w:
                    if ans[i-1][j+1] != '#':
                        ans[i-1][j+1] += 1
                if i+1 < h and j-1 >= 0:
                    if ans[i+1][j-1] != '#':
                        ans[i+1][j-1] += 1
                if i+1 < h and j+1 < w:
                    if ans[i+1][j+1] != '#':
                        ans[i+1][j+1] += 1
    for i in range(h):
        for j in range(w):
            if ans[i][j] == '#':
                print('#',end='')
            else:
                print(ans[i][j],end='')
        print()
