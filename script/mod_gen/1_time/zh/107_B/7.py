def main():
    # 读入数据
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    # 判断每行是否有黑格子
    # 判断每列是否有黑格子
    # 如果有，则输出
    # 如果没有，则不输出
    ans = []
    for i in range(h):
        if '#' in a[i]:
            ans.append(a[i])
    for i in range(w):
        for j in range(h):
            if ans[j][i] == '#':
                break
        else:
            continue
        break
    else:
        ans = []
    # 输出结果
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()