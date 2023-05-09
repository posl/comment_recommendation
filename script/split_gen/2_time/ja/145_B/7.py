def main():
    # 入力
    N = int(input())
    S = input()
    # 処理
    if N % 2 == 0:
        if S[:N//2] == S[N//2:]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
