def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 逻辑处理
    A.sort()
    if A == list(range(1, N + 1)):
        print('Yes')
    else:
        print('No')
