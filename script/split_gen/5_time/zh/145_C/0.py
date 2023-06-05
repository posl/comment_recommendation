def main():
    # 读入数据
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    # 计算路径长度
    import itertools
    sum = 0
    for perm in itertools.permutations(range(n)):
        for i in range(n-1):
            sum += ((x[perm[i]]-x[perm[i+1]])**2 + (y[perm[i]]-y[perm[i+1]])**2)**0.5
    # 输出结果
    print(sum / math.factorial(n))
