def main():
    #读取输入
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    #求出所有的图块数
    total = sum(map(sum, a))
    #如果不能整除，就不能使所有方格都有相同数量的图块，输出NO
    if total % (h * w) != 0:
        print("NO")
        return
    #求出每个方格都有多少个图块
    ave = total // (h * w)
    #求出需要移除的图块数
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += abs(a[i][j] - ave)
    print(ans // 2)

if __name__ == '__main__':
    main()