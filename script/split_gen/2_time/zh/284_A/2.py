def main():
    # 读取输入
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    # 逆序输出
    for i in range(N):
        print(S[N-i-1])
