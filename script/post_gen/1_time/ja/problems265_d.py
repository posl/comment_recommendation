Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = "No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                if (A[i]+A[j]+A[k])%P == 0 and (A[j]+A[k])%Q == 0 and (A[k])%R == 0:
                    ans = "Yes"
                    break
            if ans == "Yes":
                break
        if ans == "Yes":
            break
    print(ans)

=======
Suggestion 2

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = "No"
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] * p + a[j] * q + a[k] * r == p + q + r:
                    ans = "Yes"
                    break
    print(ans)
main()

=======
Suggestion 3

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [1, 3, 2, 2, 2, 3, 1, 4, 3, 2]
    #P = 5
    #Q = 7
    #R = 5
    #N = 10
    #print(A)
    #print(P)
    #print(Q)
    #print(R)
    #print(N)
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
    #print(A[54

=======
Suggestion 4

def main():
    n,p,q,r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = "No"
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                if a[i] * p + a[j] * q + a[k] * r == 0:
                    ans = "Yes"
                    break
    print(ans)

=======
Suggestion 5

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]
    for a in A:
        S.append(S[-1]+a)
    ans = "No"
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if P == S[i+1]-S[0] and Q == S[j+1]-S[i+1] and R == S[k+1]-S[j+1]:
                    ans = "Yes"
                    break
            if ans == "Yes":
                break
        if ans == "Yes":
            break
    print(ans)

=======
Suggestion 6

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    # 累積和の差
    D = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            D[i][j] = S[j+1] - S[i]
    # 答え
    ans = False
    # 1つ目の区間を固定
    for i in range(N-3):
        # 2つ目の区間を固定
        for j in range(i+1, N-2):
            # 3つ目の区間を固定
            for k in range(j+1, N-1):
                # 1つ目の区間と2つ目の区間の和
                p = D[0][i]
                # 2つ目の区間と3つ目の区間の和
                q = D[j][k]
                # 3つ目の区間と4つ目の区間の和
                r = D[k+1][N-1]
                # それぞれの和が条件を満たすか
                if p == P and q == Q and r == R:
                    ans = True
    if ans:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def solve():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                ans = max(ans,a[i]*p+a[j]*q+a[k]*r)
    print(ans)

=======
Suggestion 8

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        a_sum[i] = a_sum[i - 1] + a[i - 1]
    ans = -10**18
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                ans = max(ans, a_sum[i] * p + a_sum[j] * q + a_sum[k] * r)
    if ans < 0:
        print("No")
    else:
        print("Yes")

main()

=======
Suggestion 9

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,P,Q,R)
    #print(A)
    ans = "No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for l in range(k+1,N):
                    if A[i]+A[j]+A[k]+A[l] == P+Q+R:
                        ans = "Yes"
                        break
    print(ans)

=======
Suggestion 10

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    # (x,y,z,w) = (0,1,2,3) が条件を満たすか判定
    # x < y < z < w なので、x は 0, y は 1, z は 2 としておく
    # w は 3 から N-1 まで全探索
    # P, Q, R の最大値は 10^15 なので、
    # x,y,z,w の全探索で 10^15 * 10^15 * 10^15 * 10^15 となり
    # 10^64 となり、python では計算できない
    # これを解決するために、x,y,z,w のうち、
    # 一番値が大きいものを別に計算しておく
    # このとき、P, Q, R の値は x,y,z,w に依存しないので、
    # 一度計算した値をそれぞれの変数に代入しておく
    # 一番値が大きいものを計算するために、
    # x,y,z,w について、それぞれの累積和を計算しておく
    # これにより、x,y,z,w のうち、一番値が大きいものを計算する際には
    # その累積和を計算するだけでよくなる
    # また、x,y,z,w のうち、一番値が大きいものを計算する際には
    # 0 から w までの累積和から 0 から x-1 までの累積和を引けばよくなる
    # そのため、x,y,z,w のうち、一番値
