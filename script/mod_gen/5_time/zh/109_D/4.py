def main():
    #输入
    H,W = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(H)]
    #处理
    ans = []
    for h in range(H):
        for w in range(W):
            if a[h][w]%2 == 1:
                if w != W-1:
                    a[h][w+1] += 1
                    ans.append([h+1,w+1,h+1,w+2])
                elif h != H-1:
                    a[h+1][w] += 1
                    ans.append([h+1,w+1,h+2,w+1])
    #输出
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

if __name__ == '__main__':
    main()