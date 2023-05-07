def main():
    #入力
    A,B,C,D = map(int, input().split())
    #処理
    if A < C:
        print("Takahashi")
    elif A == C:
        if B < D:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        print("Aoki")
