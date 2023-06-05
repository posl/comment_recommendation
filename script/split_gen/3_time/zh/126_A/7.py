def main():
    # 读取输入
    n, k = map(int, input().split())
    s = input()
    # 按照题目要求输出
    print(s[:k-1] + s[k-1].lower() + s[k:])
