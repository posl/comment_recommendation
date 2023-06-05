def main():
    # 读入数据
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]
    # 判断有没有这个可能
    for i in range(m):
        if data[i][0] == 1 or data[i][1] == 1:
            print('Yes')
            return
    print('No')
