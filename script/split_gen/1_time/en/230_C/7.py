def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B)
    #print(P, Q, R, S)
    # 1行目の出力
    for j in range(R, S+1):
        if A <= j <= B:
            print('#', end='')
        else:
            print('.', end='')
    print()
    # 2行目以降の出力
    for i in range(P+1, Q+1):
        #print(i)
        #print(i, i-A, i-B)
        #print(i, i-A, i-B, i-A+1, i-B+1)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3, i-A+4, i-B+4)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3, i-A+4, i-B+4, i-A+5, i-B+5)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3, i-A+4, i-B+4, i-A+5, i-B+5, i-A+6, i-B+6)
        #print(i, i-A, i-B, i-A+1, i-B+1, i-A+2, i-B+2, i-A+3, i-B+3, i-A+4, i-B+4, i-A+5, i-B+5, i-A+6, i-B+6, i-A+7, i-B+7)
        #print
