def main():
    # 入力
    A,B,C,D,E = map(int, input().split())
    # 処理
    if (A == B) and (A == C) and (D == E):
        print("Yes")
    elif (A == B) and (C == D) and (C == E):
        print("Yes")
    else:
        print("No")
