def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 判断是否存在不符合条件的数字
    for i in range(n):
        if a[i] % 2 == 0 and a[i] % 3 != 0 and a[i] % 5 != 0:
            print("DENIED")
            return
    print("APPROVED")
    return
