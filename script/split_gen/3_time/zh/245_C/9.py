def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 检查是否有解
    a.sort()
    b.sort()
    for i in range(n):
        if abs(a[i] - b[i]) > k:
            print("No")
            return
    print("Yes")
