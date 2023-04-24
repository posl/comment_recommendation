Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    if N == 2:
        if x == A[0] and y == 0:
            print("Yes")
        else:
            print("No")
    elif N == 3:
        if x == A[0] + A[1] and y == A[2]:
            print("Yes")
        else:
            print("No")
    else:
        if x == A[0] + A[1] and y == A[2]:
            print("Yes")
        elif x == A[0] + A[1] + A[3] and y == A[2] + A[4]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    p = [(0, 0)]
    for a in A:
        p.append((p[-1][0] + a, 0))
    p.append((x, y))
    for i in range(N):
        if p[i][0] == p[i+1][0] and p[i+1][0] == p[i+2][0]:
            if p[i][1] <= p[i+1][1] <= p[i+2][1] or p[i][1] >= p[i+1][1] >= p[i+2][1]:
                print("No")
                exit()
        elif p[i][1] == p[i+1][1] and p[i+1][1] == p[i+2][1]:
            if p[i][0] <= p[i+1][0] <= p[i+2][0] or p[i][0] >= p[i+1][0] >= p[i+2][0]:
                print("No")
                exit()
    print("Yes")

=======
Suggestion 3

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    p = [[0, 0]]
    for i in range(N):
        if i % 2 == 0:
            p.append([p[i][0] + A[i], p[i][1]])
        else:
            p.append([p[i][0], p[i][1] + A[i]])
    p.append([x, y])
    for i in range(N):
        if p[i][0] == p[i+1][0] == p[i+2][0]:
            if not (p[i][1] < p[i+1][1] < p[i+2][1] or p[i][1] > p[i+1][1] > p[i+2][1]):
                print("No")
                return
        elif p[i][1] == p[i+1][1] == p[i+2][1]:
            if not (p[i][0] < p[i+1][0] < p[i+2][0] or p[i][0] > p[i+1][0] > p[i+2][0]):
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")
    return

main()

=======
Suggestion 4

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "Yes"
    for i in range(N):
        if A[i] > x or A[i] > y:
            ans = "No"
            break
        if i == 0:
            x -= A[i]
        else:
            if A[i] > x:
                ans = "No"
                break
            else:
                x -= A[i]
            if A[i] > y:
                ans = "No"
                break
            else:
                y -= A[i]
    print(ans)

=======
Suggestion 5

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, x, y)
    #print(A)
    #p_1 = (0, 0)
    #p_2 = (A_1, 0)
    #p_{N+1} = (x, y)
    #点 p_i と点 p_{i+1} の距離は A_i (1 ≦ i ≦ N)
    #線分 p_i p_{i+1} と線分 p_{i+1} p_{i+2} のなす角は 90 度 (1 ≦ i ≦ N - 1)
    #print(N, x, y, A)
    #print(p_1, p_2, p_N+1)
    #print(A_i, A_i

=======
Suggestion 6

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, x, y)
    #print(A)
    
    #N, x, y = 3, -1, 1
    #A = [2, 1, 3]
    #N, x, y = 5, 2, 0
    #A = [2, 2, 2, 2, 2]
    #N, x, y = 4, 5, 5
    #A = [1, 2, 3, 4]
    #N, x, y = 3, 2, 7
    #A = [2, 7, 4]
    #N, x, y = 10, 8, -7
    #A = [6, 10, 4, 1, 5, 9, 8, 6, 5, 1]
    
    # 1. p1 = (0,0) p2 = (A1, 0) pN+1 = (x, y) として、
    # 2. p1-p2, p2-pN+1, pN+1-p1 のなす角が90度であることを確認する
    # 3. p1-p2, p2-pN+1, pN+1-p1 の距離がA1, A2, A3 であることを確認する
    # 4. p1-p2, p2-p3, p3-p1 のなす角が90度であることを確認する
    # 5. p1-p2, p2-p3, p3-p1 の距離がA1, A2, A3 であることを確認する
    # 6. p1-p2, p2-p3, p3-p4, p4-p1 のなす角が90度であることを確認する
    # 7. p1-p2, p2-p3, p3-p4,

=======
Suggestion 7

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, x, y, A)
    #print(A)
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64])
    #

=======
Suggestion 8

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 90度の判定
    def judge90(x1, y1, x2, y2):
        if x1 * x2 + y1 * y2 == 0:
            return True
        else:
            return False
    
    # 2点間の距離の判定
    def judgeDist(x1, y1, x2, y2, dist):
        if (x1 - x2)**2 + (y1 - y2)**2 == dist**2:
            return True
        else:
            return False
    
    # 答え
    ans = "Yes"
    
    # 初期値
    x1, y1 = 0, 0
    x2, y2 = A[0], 0
    # 2点間の距離の判定
    if not judgeDist(x1, y1, x2, y2, A[0]):
        ans = "No"
    # 90度の判定
    if not judge90(x2, y2, x, y):
        ans = "No"
    
    for i in range(1, N):
        # 2点間の距離の判定
        if not judgeDist(x2, y2, x, y, A[i]):
            ans = "No"
        # 90度の判定
        if not judge90(x1, y1, x2, y2):
            ans = "No"
        
        x1, y1 = x2, y2
        x2, y2 = x, y
    
    # 2点間の距離の判定
    if not judgeDist(x2, y2, x, y, A[N-1]):
        ans = "No"
    
    print(ans)

=======
Suggestion 9

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    # 1. p1 = (0, 0) からスタート
    # 2. p2 = (A1, 0) になるように移動
    # 3. p3 = (A1, A2) になるように移動
    # 4. p4 = (A1, A2 + A3) になるように移動
    # 5. p5 = (A1 + A4, A2 + A3) になるように移動
    # 6. p6 = (A1 + A4, A2 + A3 + A5) になるように移動
    # 7. p7 = (A1 + A4 + A6, A2 + A3 + A5) になるように移動
    # 8. p8 = (A1 + A4 + A6, A2 + A3 + A5 + A7) になるように移動
    # 9. p9 = (A1 + A4 + A6 + A8, A2 + A3 + A5 + A7) になるように移動
    # 10. p10 = (A1 + A4 + A6 + A8, A2 + A3 + A5 + A7 + A9) になるように移動
    # 11. p11 = (x, y) になるように移動
    # 12. p11 と p1 の距離が A1 であることを確認
    # 13. p1 と p2 の距離が A2 であることを確認
    # 14. p2 と p3 の距離が A3 であることを確認
    # 15. p3 と p4 の距離が A4 であることを確

=======
Suggestion 10

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))

    # 0.0 から 0.0 に向かって、A[0] の距離だけ進む。
    # その後、A[1] の距離だけ進む。
    # その後、A[2] の距離だけ進む。
    # ・・・
    # その後、A[N-1] の距離だけ進む。
    # その後、A[N] の距離だけ進む。
    # その後、x の距離だけ進む。
    # その後、y の距離だけ進む。
    # ・・・
    # その後、A[0] の距離だけ戻る。
    # その後、A[1] の距離だけ戻る。
    # ・・・
    # その後、A[N-1] の距離だけ戻る。
    # その後、A[N] の距離だけ戻る。
    # その後、0.0 の距離だけ戻る。
    # ・・・
    # その後、A[0] の距離だけ進む。
    # その後、A[1] の距離だけ進む。
    # ・・・
    # その後、A[N-1] の距離だけ進む。
    # その後、A[N] の距離だけ進む。
    # その後、x の距離だけ進む。
    # その後、y の距離だけ進む。
    # ・・・
    # その後、A[0] の距離だけ戻る。
    # その後、A[1] の距離だけ戻る。
    # ・・・
    # その後、
