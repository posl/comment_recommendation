Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < L:
            ans += L
        elif A[i] > R:
            ans += R
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[:N // 2]) * L + sum(A[N // 2:]) * R)

=======
Suggestion 3

def main():
    #入力
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #初期化
    ans = 0
    #処理
    #Aの要素の総和を求める
    for i in range(N):
        ans += A[i]
    #x=1~N,y=1~Nの場合の総和を求める
    for i in range(1,N+1):
        for j in range(1,N+1):
            #Aの要素をL,Rで置き換える
            for k in range(i):
                A[k] = L
            for k in range(j):
                A[N-1-k] = R
            #Aの要素の総和を求める
            tmp = 0
            for k in range(N):
                tmp += A[k]
            #最小値を求める
            if tmp < ans:
                ans = tmp
    #出力
    print(ans)

=======
Suggestion 4

def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    print(sum(A[:N//2])*L+sum(A[N//2:])*R)
main()

=======
Suggestion 5

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #累積和を求める
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i]+A[i])

    #すべてのx,yについて、累積和の差を求める
    ans = 10**9
    for x in range(N+1):
        for y in range(N+1):
            if x+y > N:
                break
            #累積和の差を求める
            diff = cumsum[N]-cumsum[N-y]-cumsum[x]
            #x,yの操作の結果
            #xが0の場合は、A_1,A_2,...,A_N
            #yが0の場合は、A_{N},A_{N-1},...,A_{N-y+1}
            #それ以外の場合は、A_1,A_2,...,A_x,L,A_{N},A_{N-1},...,A_{N-y+1},R
            if x == 0:
                if y == 0:
                    #x,yともに0の場合は、A_1,A_2,...,A_N
                    #何もしないので、diffはそのまま
                    pass
                else:
                    #xが0,yが0以外の場合は、A_1,A_2,...,A_N,R
                    #yの個数分、Rを引く
                    diff -= R*y
            else:
                if y == 0:
                    #xが0以外,yが0の場合は、A_1,A_2,...,A_x,L
                    #xの個数分、Lを足す
                    diff += L*x
                else:
                    #x,yともに0以外の場合は、A_1,A_2,...,A_x,L,A_{N},A_{N-1},...,A_{N-y+1},R
                    #xの個数分、Lを足す
                    diff += L*x
                    #yの

=======
Suggestion 6

def main():
    # 入力
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # 操作前の A の要素の総和
    S = sum(A)
    # 操作後の A の要素の総和の最小値
    ans = 10**18
    # x を 0 から N まで試す
    for x in range(N+1):
        # x として 0 を選んだ場合
        if x == 0:
            # 操作後の A の要素の総和
            T = S
            # y を 0 から N まで試す
            for y in range(N+1):
                # y として 0 を選んだ場合
                if y == 0:
                    # 操作後の A の要素の総和の最小値を更新
                    ans = min(ans, T)
                # y として 1 以上の整数を選んだ場合
                else:
                    # 操作後の A の要素の総和
                    T += R - A[N-y]
                    # 操作後の A の要素の総和の最小値を更新
                    ans = min(ans, T)
        # x として 1 以上の整数を選んだ場合
        else:
            # 操作後の A の要素の総和
            T = S + L * x - sum(A[:x])
            # y を 0 から N まで試す
            for y in range(N+1):
                # y として 0 を選んだ場合
                if y == 0:
                    # 操作後の A の要素の総和の最小値を更新
                    ans = min(ans, T)
                # y として 1 以上の整数を選んだ場合
                else:
                    # 操作後の A の要素の総和
                    T += R - A[N-y]
                    # 操作後の

=======
Suggestion 7

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, L, R)
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

    #print(A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] + A[7] + A[8] + A[9] + A[10])
    #print(sum(A))

    #print(A[0:1])
    #print(A[0:2])
    #print(A[0:3])
    #print(A[0:4])
    #print(A[0:5])
    #print(A[0:6])
    #print(A[0:7])
    #print(A[0:8])
    #print(A[0:9])
    #print(A[0:10])
    #print(A[0:11])

    #print(A[1:2])
    #print(A[1:3])
    #print(A[1:4])
    #print(A[1:5])
    #print(A[1:6])
    #print(A[1:7])
    #print(A[1:8])
    #print(A[1:9])
    #print(A[1:10])
    #print(A[1:11])

    #print(A[2:3])
    #print(A[2:4])
    #print(A[2:5])
    #print(A[2:6])
    #print(A[2:7])
    #print(A[2:8])
    #print(A[2:9])
    #print(A[2:10])
    #print(A[2:11])

    #print(A[3:4])
    #print(A[3:5])
    #print(A[3:6])
    #print(A[3:7])
    #print(A[3:8])
    #print(A

=======
Suggestion 8

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, L, R)
    #print(A)
    #print(sum(A))
    #print(min(A))

    if L > R:
        L,R = R,L
    if L >= 0:
        print(sum(A) + N*L)
        return
    if R <= 0:
        print(sum(A) + N*R)
        return
    #ここまでで、L,Rは0を含む
    #print(sum(A))
    #print(sum(A) + N*L)
    #print(sum(A) + N*R)
    #print(sum(A) + N*(L+R)//2)
    #print(N*(L+R)//2)

    #ここから、L,Rは0を含む
    #A_i>0の時、A_iをLで置き換える
    #A_i<0の時、A_iをRで置き換える
    #A_i=0の時、A_iをL,Rのうち小さい方で置き換える
    #A_i=0の時、A_iをL,Rのうち大きい方で置き換える

    #A_i>0の時、A_iをLで置き換える
    #A_i<0の時、A_iをRで置き換える
    #A_i=0の時、A_iをL,Rのうち小さい方で置き換える
    #A_i=0の時、A_iをL,Rのうち大きい方で置き換える
    #print(min(A))
    #print(max(A))
    #print(L)
    #print(R)

    #A_i=0の時、A_iをL,Rのうち小さい方で置き換える
    #A_i=0の時、A_iをL,Rのうち大きい方で置き換える
    #print(N)
    #print(L)
    #print(R)
    #print(A)
    #print(sum(A))

    #A_i=0の時、

=======
Suggestion 9

def main():
    N,L,R=map(int,input().split())
    A=list(map(int,input().split()))
    #print(N,L,R,A)
    S=sum(A)
    #print(S)
    #print("max",max(A))
    #print("min",min(A))
    #print("max-min",max(A)-min(A))
    #print("sum",sum(A))
    #print("max-min-sum",max(A)-min(A)+sum(A))
    #print("max-min-sum/2",int((max(A)-min(A)+sum(A))/2))
    #print("max-min-sum/2+min",int((max(A)-min(A)+sum(A))/2)+min(A))
    #print("max-min-sum/2+min-max",int((max(A)-min(A)+sum(A))/2)+min(A)-max(A))
    if L==R:
        print(N*L)
    elif L>R:
        if max(A)-min(A)+sum(A) >= 0:
            print(int((max(A)-min(A)+sum(A))/2)+min(A)-max(A))
        else:
            print(int((max(A)-min(A)+sum(A))/2)+min(A)-max(A)+N*R)
    else:
        if max(A)-min(A)+sum(A) >= 0:
            print(int((max(A)-min(A)+sum(A))/2)+min(A)-max(A))
        else:
            print(int((max(A)-min(A)+sum(A))/2)+min(A)-max(A)+N*L)
