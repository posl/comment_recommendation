def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    print(s)
    # 从两个棋子开始搜索
    # 搜索的时候记录已经走过的路，防止重复搜索
    # 搜索到另一个棋子的时候，记录步数
    # 用一个数组来

if __name__ == '__main__':
    main()