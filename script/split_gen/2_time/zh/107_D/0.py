def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    
    # 保存中位数
    m = []
    for i in range(n):
        temp = a[i]
        for j in range(i+1, n):
            temp = temp + a[j]
            m.append(temp)
    
    # 排序
    m.sort()
    
    # 输出
    print(m[int(len(m)/2)])
