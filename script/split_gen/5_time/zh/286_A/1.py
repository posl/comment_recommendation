def main():
    # 读取数据
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    # 交换
    b = a[0:p-1]+a[r-1:s]+a[q-1:r-1]+a[p-1:q-1]+a[s:]
    # 打印
    for i in range(n):
        if i == n-1:
            print(b[i])
        else:
            print(b[i], end=" ")
