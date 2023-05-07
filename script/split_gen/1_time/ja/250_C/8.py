def main():
    N, Q = map(int, input().split())
    #ボールの初期位置
    ball = [i for i in range(1, N+1)]
    #ボールの最終位置
    result = [0 for i in range(N)]
    #ボールの最終位置を求める
    for i in range(Q):
        x = int(input())
        #ボールの位置を入れ替える
        ball[x-1], ball[x] = ball[x], ball[x-1]
    #ボールの最終位置を求める
    for i in range(N):
        result[ball[i]-1] = i+1
    #出力
    print(*result)
