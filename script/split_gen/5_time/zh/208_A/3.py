def main():
    #输入
    A, B = map(int, input().split())
    #处理
    if A <= B <= 6 * A:
        print("Yes")
    else:
        print("No")
    #输出
