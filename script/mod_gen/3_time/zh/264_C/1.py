def main():
    # 读取数据
    h1, w1 = map(int, input().split())
    a = []
    for i in range(h1):
        a.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    b = []
    for i in range(h2):
        b.append(list(map(int, input().split())))
    # 从a中删除h2行w2列
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            # 从a中删除h2行w2列
            c = [a[i + k][j:j + w2] for k in range(h2)]
            # 判断c是否等于b
            if c == b:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()