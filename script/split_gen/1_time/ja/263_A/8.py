def main():
    #入力
    A,B,C,D,E = map(int,input().split())
    #フルハウスかどうかを判定
    if A == B and B == C and (D == E or D != E):
        print("Yes")
    elif A == B and B != C and (C == D and D == E):
        print("Yes")
    elif A != B and (B == C and C == D and D != E):
        print("Yes")
    elif A != B and (B != C and C == D and D == E):
        print("Yes")
    else:
        print("No")
