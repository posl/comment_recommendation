def main():
    #H: number of rows
    #W: number of columns
    #A: number of blocks in each square
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #count: count of each number of blocks
    count = [0] * 101
    #count the number of blocks in each square
    for i in range(H):
        for j in range(W):
            count[A[i][j]] += 1
    #ans: the minimum number of blocks that must be removed
    ans = 10**6
    #try each number of blocks
    for i in range(101):
        #blocks: number of blocks to be removed
        #num: number of squares with i blocks
        blocks = 0
        num = 0
        for j in range(101):
            #if number of blocks is j, remove (j-i) blocks from each square
            if j > i:
                blocks += (j-i) * count[j]
            #if number of blocks is j, add j blocks to each square
            else:
                num += count[j]
        #if the number of blocks is i, the number of blocks to be removed is blocks
        if num == H * W:
            ans = min(ans, blocks)
    print(ans)

if __name__ == '__main__':
    main()