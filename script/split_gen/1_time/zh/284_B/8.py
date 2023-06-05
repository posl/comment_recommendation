def main():
    # 读取数据
    t = int(input())
    n = []
    a = []
    for i in range(t):
        n.append(int(input()))
        a.append(list(map(int, input().split())))
    # 处理数据
    for i in range(t):
        count = 0
        for j in range(n[i]):
            if a[i][j] % 2 == 1:
                count += 1
        print(count)
