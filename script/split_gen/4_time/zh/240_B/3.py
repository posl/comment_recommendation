def main():
    # 输入
    N = int(input())
    a = list(map(int, input().split()))
    # 处理
    a.sort()
    # 输出
    print(len(set(a)))
