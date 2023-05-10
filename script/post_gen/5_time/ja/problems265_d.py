Synthesizing 9/10 solutions

=======
Suggestion 1

def get_input():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    return N, P, Q, R, A

=======
Suggestion 2

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 'No'
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if (A[i] + A[i+1] + ... + A[j-1]) == P and (A[j] + A[j+1] + ... + A[k-1]) == Q and (A[k] + A[k+1] + ... + A[l-1]) == R:
                        ans = 'Yes'
                        break
    print(ans)

=======
Suggestion 3

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 'No'
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if i < j < k < l:
                        if A[i] + A[i+1] + A[j-1] == P:
                            if A[j] + A[j+1] + A[k-1] == Q:
                                if A[k] + A[k+1] + A[l-1] == R:
                                    ans = 'Yes'
    print(ans)

=======
Suggestion 4

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # x < y < z < w
    # A_x + A_{x+1} + ... + A_{y-1} = P
    # A_y + A_{y+1} + ... + A_{z-1} = Q
    # A_z + A_{z+1} + ... + A_{w-1} = R

    # 1 <= x < y < z < w <= N
    # 1 <= A_i <= 10^9
    # 1 <= P,Q,R <= 10^15
    # 入力に含まれる値は全て整数である

    # 1 <= x < y < z < w <= N
    # 1 <= A_i <= 10^9
    # 1 <= P,Q,R <= 10^15
    # 入力に含まれる値は全て整数である

    # 1 <= x < y < z < w <= N
    # 1 <= A_i <= 10^9
    # 1 <= P,Q,R <= 10^15
    # 入力に含まれる値は全て整数である

    # 1 <= x < y < z < w <= N
    # 1 <= A_i <= 10^9
    # 1 <= P,Q,R <= 10^15
    # 入力に含まれる値は全て整数である

    # 1 <= x < y < z < w <= N
    # 1 <= A_i <= 10^9
    # 1 <= P,Q,R <= 10^15
    # 入力に含まれる値は全て整数である

    # 1 <= x < y < z < w <= N
    # 1 <= A_i <= 10^9
    # 1 <= P,Q,R <= 10^15
    # 入力に含まれる値は全て整数である

    # 1 <= x < y < z

=======
Suggestion 5

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    if N == 2:
        if A[0] + A[1] == P and A[0] + A[1] == Q and A[0] + A[1] == R:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 6

def solve():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))

    #累積和
    s = [0]*(N+1)
    for i in range(N):
        s[i+1] = s[i] + A[i]

    #Qを固定して考える
    #Qより前にPより大きい値があると条件を満たす組が存在する
    #Qより後にRより大きい値があると条件を満たす組が存在する
    #Qより後にPより小さい値があると条件を満たす組が存在する
    #Qより前にRより小さい値があると条件を満たす組が存在する
    #Qより前にPより大きくRより大きい値があると条件を満たす組が存在する
    #Qより後にPより小さくRより小さい値があると条件を満たす組が存在する
    #Qより前にPより大きくRより小さい値があると条件を満たす組が存在する
    #Qより後にPより小さくRより大きい値があると条件を満たす組が存在する

    #Qより前にPより大きい値があると条件を満たす組が存在する
    for i in range(N):
        if s[i] > P:
            break
        if s[i] < P:
            continue
        for j in range(i+1,N):
            if s[j] > P:
                break
            if s[j] < P:
                continue
            if s[j] - s[i] == P:
                for k in range(j+1,N):
                    if s[k] > Q:
                        break
                    if s[k] < Q:
                        continue
                    if s[k] - s[j] == Q:
                        for l in range(k+1,N

=======
Suggestion 7

def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    ans = "No"
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if (a[i]+a[i+1]+a[j]+a[j+1]+a[k]+a[k+1]) == p and (a[j]+a[j+1]+a[k]+a[k+1]+a[l]+a[l+1]) == q and (a[k]+a[k+1]+a[l]+a[l+1]+a[i]+a[i+1]) == r:
                        ans = "Yes"
                        break
    print(ans)

=======
Suggestion 8

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    res = 10**100
    for i in range(N-3+1):
        for j in range(i+1,N-2+1):
            for k in range(j+1,N-1+1):
                for l in range(k+1,N+1):
                    tmp = abs(P-A[i]*(j-i)+Q-A[j]*(k-j)+R-A[k]*(l-k))
                    if tmp < res:
                        res = tmp
    print(res)

=======
Suggestion 9

def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,p,q,r,a)
    #print(len(a))
    #print(a[0])
    #print(a[1])
    #print(a[2])
    #print(a[3])
    #print(a[4])
    #print(a[5])
    #print(a[6])
    #print(a[7])
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(a[12])
    #print(a[13])
    #print(a[14])
    #print(a[15])
    #print(a[16])
    #print(a[17])
    #print(a[18])
    #print(a[19])
    #print(a[20])
    #print(a[21])
    #print(a[22])
    #print(a[23])
    #print(a[24])
    #print(a[25])
    #print(a[26])
    #print(a[27])
    #print(a[28])
    #print(a[29])
    #print(a[30])
    #print(a[31])
    #print(a[32])
    #print(a[33])
    #print(a[34])
    #print(a[35])
    #print(a[36])
    #print(a[37])
    #print(a[38])
    #print(a[39])
    #print(a[40])
    #print(a[41])
    #print(a[42])
    #print(a[43])
    #print(a[44])
    #print(a[45])
    #print(a[46])
    #print(a[47])
    #print(a[48])
    #print(a[49])
    #print(a[50])
    #print(a[51])
    #print(a[52])
    #print(a[53])
    #print(a[54])
    #print(a[55])
    #print(a[56])
    #print(a[57])
    #print(a[58])
    #print(a[59])
    #print(a[60])
    #print(a[61])
    #print(a[62])
    #print(a[63])
    #print(a[64])
    #print(a[65
