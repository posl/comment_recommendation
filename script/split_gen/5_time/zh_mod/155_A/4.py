def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 决定输出
    if A == B and B != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    el
