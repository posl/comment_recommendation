def main():
    # 读取输入
    line = input()
    line = line.split()
    n = int(line[0])
    m = int(line[1])
    line = input()
    line = line.split()
    a = []
    for i in range(m):
        a.append(int(line[i]))
    # 处理
    a.sort()
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum > n:
        print(-1)
    else:
        print(n - sum)
