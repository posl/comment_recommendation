def main():
    #读取数据
    h,w = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    #print(s)
    #计算
    #每行的最左边的'#'到最右边的'#'的距离
    #每列的最上边的'#'到最下边的'#'的距离
    left = [[0]*w for i in range(h)]
    right = [[0]*w for i in range(h)]
    up = [[0]*w for i in range(h)]
    down = [[0]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            #print(i,j)
            if s[i][j] == '#':
                left[i][j] = 0
            else:
                if j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j-1] + 1
    for i in range(h):
        for j in range(w-1,-1,-1):
            #print(i,j)
            if s[i][j] == '#':
                right[i][j] = 0
            else:
                if j == w-1:
                    right[i][j] = 1
                else:
                    right[i][j] = right[i][j+1] + 1
    for j in range(w):
        for i in range(h):
            #print(i,j)
            if s[i][j] == '#':
                up[i][j] = 0
            else:
                if i == 0:
                    up[i][j] = 1
                else:
                    up[i][j] = up[i-1][j] + 1
    for j in range(w):
        for i in range(h-1,-1,-1):
            #print(i,j)
            if s[i][j] == '#':
                down[i][j] = 0
            else:
                if i == h-1:
                    down[i][j] = 1
                else:
                    down[i][j] = down[i+1][j] + 1
    #print(left)
    #print(right)
    #print(up

if __name__ == '__main__':
    main()