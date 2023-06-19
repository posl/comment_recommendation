def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    # 解决问题
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print("No")
            exit()
    print("Yes")
