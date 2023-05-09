def main():
    #入力
    N = int(input())
    S, T = input().split()
    #出力
    print("".join(S[i] + T[i] for i in range(N)))
