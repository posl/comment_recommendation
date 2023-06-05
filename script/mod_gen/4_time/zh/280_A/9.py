def main():
    # 读取输入
    h, w = map(int, input().split())
    # 用列表保存输入的字符串
    s = []
    for i in range(h):
        s.append(input())
    # 计数器
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    print(count)
main()
