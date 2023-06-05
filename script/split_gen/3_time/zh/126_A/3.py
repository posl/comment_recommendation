def main():
    # 读取输入
    N, K = map(int, input().split())
    S = input()
    # 通过列表解析替换第K个字符
    S_new = S[:K-1] + S[K-1].lower() + S[K:]
    print(S_new)
