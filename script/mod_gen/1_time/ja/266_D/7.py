def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    T_X_A = [list(map(int, input().split())) for _ in range(N)]
    #print(T_X_A)
    #print(N)
    #print(T_X_A[0])
    #print(T_X_A[0][0])
    #print(T_X_A[0][1])
    #print(T_X_A[0][2])
    #print(T_X_A[0][1] == T_X_A[1][1])
    #print(T_X_A[0][0] == T_X_A[1][0])
    #print(T_X_A[0][1] == T_X_A[1][1] and T_X_A[0][0] == T_X_A[1][0])
    #1つ目のすぬけ君の座標
    X1 = T_X_A[0][1]
    #1つ目のすぬけ君の大きさ
    A1 = T_X_A[0][2]
    #1つ目のすぬけ君の出現時刻
    T1 = T_X_A[0][0]
    #print(X1)
    #print(A1)
    #print(T1)
    #2つ目のすぬけ君の座標
    X2 = T_X_A[1][1]
    #2つ目のすぬけ君の大きさ
    A2 = T_X_A[1][2]
    #2つ目のすぬけ君の出現時刻
    T2 = T_X_A[1][0]
    #print(X2)
    #print(A2)
    #print(T2)
    #3つ目のすぬけ君の座標
    X3 = T_X_A[2][1]
    #3つ目のすぬけ君の大きさ
    A3 = T_X_A[2][2]
    #3つ目のすぬけ君の出現時刻
    T3 = T_X_A[2][0]
    #print(X3)
    #print(A3)
    #print(T3

if __name__ == '__main__':
    main()