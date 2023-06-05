def main():
    # 读取输入
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    
    # 生成和的集合
    s = set()
    for i in range(n):
        for j in range(i + 1, n):
            s.add(a[i] + a[j])
    
    # 找出最大的D的倍数
    result = -1
    for x in s:
        if x % d == 0:
            result = max(result, x)
    
    # 打印答案
    print(result)

if __name__ == '__main__':
    main()