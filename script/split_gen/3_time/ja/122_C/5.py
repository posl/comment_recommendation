def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]
    #ACの出現回数を数える
    AC_count = 0
    AC_list = [0] * N
    for i in range(N-1):
        if S[i:i+2] == "AC":
            AC_count += 1
        AC_list[i+1] = AC_count
    #出力
    for l, r in LR:
        print(AC_list[r-1] - AC_list[l-1])
