def main():
    S = input("输入字符串S：")
    for i in range(10):
        if str(i) not in S:
            print(i)
            break
