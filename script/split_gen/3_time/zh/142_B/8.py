def main():
    # 读入数据
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    # 遍历数据
    count = 0
    for i in h:
        if i >= k:
            count += 1
    
    # 打印结果
    print(count)
