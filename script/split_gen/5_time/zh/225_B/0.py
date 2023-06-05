def main():
    # 读入数据
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    # 初始化
    d = [0 for i in range(N)]
    # 统计
    for i in range(N-1):
        d[a[i]-1] += 1
        d[b[i]-1] += 1
    # 判断
    if max(d) == N-1:
        print('Yes')
    else:
        print('No')
