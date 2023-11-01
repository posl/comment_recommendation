def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    # print(S)
    # print(set(S))
    # print(len(set(S)))
    # 1. 有重复的字符串
    if len(set(S)) < N:
        # print("1")
        # 1.1 有多个重复的字符串
        if len(set(S
