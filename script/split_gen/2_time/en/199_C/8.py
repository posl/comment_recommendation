def main():
    N = int(input())
    S = input()
    Q = int(input())
    T_A_B = [list(map(int,input().split())) for _ in range(Q)]
    S = list(S)
    S1 = S[:N]
    S2 = S[N:]
    C = 0 # 1: S1,S2の入れ替え
    for t,a,b in T_A_B:
        if t == 1:
            if C == 0:
                S1[a-1],S1[b-1] = S1[b-1],S1[a-1]
            else:
                S2[a-1],S2[b-1] = S2[b-1],S2[a-1]
        else:
            C = 1-C
    if C == 0:
        print("".join(S1+S2))
    else:
        print("".join(S2+S1))
