def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M)
    #print(A)
    # ボールの色をキーにして、ボールの個数を値とする辞書
    ball = {}
    for i in range(M):
        for j in range(1, A[i][0]+1):
            if A[i][j] in ball:
                ball[A[i][j]] += 1
            else:
                ball[A[i][j]] = 1
    #print(ball)
    # ボールの個数が奇数個であるとき、目標を達成することができない
    for b in ball:
        if ball[b] % 2 == 1:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()