def main():
    # 读入数据
    N = int(input())
    S = input()
    # 用.替换S中每一个不是封闭字符的"
    for i in range(N):
        if S[i] == '"' and i % 2 == 1:
            S = S[:i] + '.' + S[i+1:]
    # 打印答案
    print(S)
