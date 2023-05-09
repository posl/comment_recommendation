def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    # 人数が 2 人の場合
    if N == 2:
        # 2 人の人が同じ向きに歩いている場合
        if S[0] == S[1]:
            print("No")
        # 2 人の人が異なる向きに歩いている場合
        else:
            # 2 人の人が同じ地点にいる場合
            if X[0] == X[1] and Y[0] == Y[1]:
                print("Yes")
            # 2 人の人が異なる地点にいる場合
            else:
                print("No")
    # 人数が 3 人以上の場合
    else:
        # 人数が 3 人の場合
        if N == 3:
            # 3 人の人が同じ向きに歩いている場合
            if S[0] == S[1] and S[0] == S[2]:
                print("No")
            # 3 人の人が異なる向きに歩いている場合
            else:
                # 3 人の人が同じ地点にいる場合
                if X[0] == X[1] and Y[0] == Y[1] or X[0] == X[2] and Y[0] == Y[2] or X[1] == X[2] and Y[1] == Y[2]:
                    print("Yes")
                # 3 人の人が異なる地点にいる場合
                else:
                    print("No")
        # 人数が 4 人以上の場合
        else:
            # 4 人の人が同じ向きに歩いている場合
            if S[0] == S[1] and S[

if __name__ == '__main__':
    main()