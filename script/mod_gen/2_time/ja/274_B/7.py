def main():
    h,w = map(int,input().split())
    grid = [list(input()) for _ in range(h)]
    w_lst = [0]*w
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
                w_lst[j] += 1
    print(*w_lst)

if __name__ == '__main__':
    main()