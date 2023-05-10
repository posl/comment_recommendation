def solve():
    # === 数値変数の入力 ===
    # N = int(input())  # 1つの整数
    # L, R = map(int, input().split())  # 複数の整数
    # a = list(map(int, input().split()))  # 複数の整数
    S = input()  # 1つの文字列
    # === 行列の入力 ===
    # A = []
    # for i in range(N):
    #     A.append(list(map(int, input().split())))  # 複数の整数(スペース区切り)を受け取る
    # A = [list(map(int, input().split())) for i in range(N)]  # 複数の整数(スペース区切り)を受け取る
    # ここに書く
    if S[0] == S[1] == S[2]:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    solve()