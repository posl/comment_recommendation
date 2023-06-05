def main():
    # 请在此添加代码
    n = int(input())
    if -2**31 <= n and n <= 2**31-1:
        print("是")
    else:
        print("否")
main()
