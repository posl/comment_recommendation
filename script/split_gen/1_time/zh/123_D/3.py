def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    # 从大到小排序
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    # 从大到小排序
    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i] + b[j])
    ab.sort(reverse=True)
    # 从大到小排序
    abc = []
    for i in range(min(k, x * y)):
        for j in range(z):
            abc.append(ab[i] + c[j])
    abc.sort(reverse=True)
    # 输出
    for i in range(k):
        print(abc[i])
