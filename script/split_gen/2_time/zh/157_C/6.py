def main():
    # 读取输入
    a = []
    for i in range(3):
        a.append([int(x) for x in input().split()])
    n = int(input())
    b = []
    for i in range(n):
        b.append(int(input()))
    # 计算结果
    result = 'No'
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                result = 'Yes'
                break
        if result == 'Yes':
            break
    # 输出结果
    print(result)
