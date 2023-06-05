Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    #print(n, x, ab)
    a = [i[0] for i in ab]
    b = [i[1] for i in ab]
    #print(a, b)
    if sum(a) + sum(b) <= x:
        print(2 * n)
        return
    elif sum(a) > x:
        print(0)
        return
    else:
        for i in range(n):
            if sum(a[:i+1]) + sum(b[:i+1]) > x:
                print(2 * i + 1)
                return
            elif sum(a[:i+1]) + sum(b[:i+1]) == x:
                print(2 * i + 2)
                return
            else:
                pass
        print(2 * n)

=======
Suggestion 2

def solve():
    N,X = map(int,input().split())
    A = []
    B = []
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    # print(X)
    ans = 10**18
    for i in range(N):
        t = A[i]
        ans = min(ans,t*X)
        t = A[i] + B[i]
        ans = min(ans,t*X + A[i])
        t = A[i] + B[i] + B[i]
        ans = min(ans,t*X + A[i] + B[i])
        t = A[i] + B[i] + B[i] + B[i]
        ans = min(ans,t*X + A[i] + B[i] + B[i])
    print(ans)

=======
Suggestion 3

def main():
    n,x=map(int,input().split())
    a=[0]*n
    b=[0]*n
    for i in range(n):
        a[i],b[i]=map(int,input().split())

    a_b=[0]*n
    for i in range(n):
        a_b[i]=a[i]+b[i]

    #print(a_b)

    max_time=max(a_b)
    #print(max_time)

    max_time_index=a_b.index(max_time)
    #print(max_time_index)

    if x==1:
        print(max_time)
        return

    if max_time_index==n-1:
        print(max_time*x)
        return

    if x==2:
        print(max_time*2)
        return

    if max_time_index==0:
        print(max_time*x)
        return

    if x==3:
        print(max_time*2)
        return

    if max_time_index==1:
        print(max_time*2)
        return

    if x==4:
        print(max_time*2)
        return

    if max_time_index==2:
        print(max_time*2)
        return

    if x==5:
        print(max_time*2)
        return

    if max_time_index==3:
        print(max_time*2)
        return

    if x==6:
        print(max_time*2)
        return

    if max_time_index==4:
        print(max_time*2)
        return

    if x==7:
        print(max_time*2)
        return

    if max_time_index==5:
        print(max_time*2)
        return

    if x==8:
        print(max_time*2)
        return

    if max_time_index==6:
        print(max_time*2)
        return

    if x==9:
        print(max_time*2)
        return

    if max_time_index==7:
        print(max_time*2)
        return

    if x==10:
        print(max_time*2)
        return

    if max_time_index==8:
        print(max_time*2)
        return

    if x==11:
        print(max_time*2)
        return

    if max_time_index==9:
        print(max_time*2)
        return

    if x==12:
        print(max_time*2)
        return

    if max_time

=======
Suggestion 4

def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]

    # 二分探索
    def is_ok(k):
        # k 分内にクリアできるステージ数
        # k 分内にクリアできるステージの回数
        cnt = 0
        for i in range(N):
            # 難易度が A[i] であるステージを k 分以内にクリアできるか？
            # k 分以内にステージをクリアできる場合
            if k - A[i] >= 0:
                # k - A[i] 分以内に B[i] 回クリアできる
                cnt += (k - A[i]) // B[i] + 1
            # k 分以内にステージをクリアできない場合
            else:
                # 何もしない
                pass
        # k 分以内にクリアできるステージの回数が X 回以上である場合
        if cnt >= X:
            return True
        # k 分以内にクリアできるステージの回数が X 回未満である場合
        else:
            return False

    # 二分探索
    # left は is_ok が True を返す最小の入力値-1
    # right は is_ok が False を返す最大の入力値+1
    left = -1
    right = 10 ** 18
    while right - left > 1:
        mid = left + (right - left) // 2
        # mid 分以内にクリアできるステージの回数が X 回以上である場合
        if is_ok(mid):
            right = mid
        # mid 分以内にクリアできるステージの回数が

=======
Suggestion 5

def solve():
    N,X=map(int,input().split())
    A=[0]*N
    B=[0]*N
    for i in range(N):
        A[i],B[i]=map(int,input().split())
    #print(A,B)
    #print(N,X)
    #print(X)
    #print(A[0]+B[0])
    #print(A[0]+B[0]+A[1]+B[1])
    #print(A[0]+B[0]+A[1]+B[1]+A[2]+B[2])
    #print(A[0]+B[0]+A[1]+B[1]+A[2]+B[2]+A[3]+B[3])
    #print(A[0]+B[0]+A[1]+B[1]+A[2]+B[2]+A[3]+B[3]+A[4]+B[4])
    #print(A[0]+B[0]+A[1]+B[1]+A[2]+B[2]+A[3]+B[3]+A[4]+B[4]+A[5]+B[5])
    #print(A[0]+B[0]+A[1]+B[1]+A[2]+B[2]+A[3]+B[3]+A[4]+B[4]+A[5]+B[5]+A[6]+B[6])
    #print(A[0]+B[0]+A[1]+B[1]+A[2]+B[2]+A[3]+B[3]+A[4]+B[4]+A[5]+B[5]+A[6]+B[6]+A[7]+B[7])
    #print(A[0]+B[0]+A[1]+B[1]+A[2]+B[2]+A[3]+B[3]+A[4]+B[4]+A[5]+B[5]+A[6]+B[6]+A[7]+B[7]+A[8]+B[8])
    #print(A[0]+B[0]+A[1]+B[1]+A[2]+B[2]+A[3]+B[3]+A[4]+B[4]+A[5]+B[5

=======
Suggestion 6

def solve(n,x,ab):
    a = [0] * (n+1)
    b = [0] * (n+1)
    for i in range(n):
        a[i+1] = ab[i][0]
        b[i+1] = ab[i][1]
    ans = 0
    for i in range(1,n+1):
        ans += a[i] + b[i]
    for k in range(1,n+1):
        ans = min(ans, x * a[k] + b[k] * (n - x))
    return ans

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    ans = 0
    for a, b in ab:
        ans += a + b
    ans += x * ab[-1][0]
    print(ans)

=======
Suggestion 8

def solve(n,x,ab):
    #先算出第一次全部通关的时间
    time = 0
    for i in range(n):
        time += ab[i][0] + ab[i][1]
    #print(time)
    #如果x大于第一次通关的时间，那么直接输出
    if x > time:
        return time
    #如果x小于第一次通关的时间，那么需要计算x次通关的时间
    else:
        #先计算出x次通关的最小时间
        time = 0
        for i in range(n):
            time += ab[i][0]
        #print(time)
        #如果x次通关的最小时间大于x，那么直接输出x
        if time > x:
            return x
        #如果x次通关的最小时间小于x，那么需要计算x次通关的时间
        else:
            #先计算出x次通关的最大时间
            time = 0
            for i in range(n):
                time += ab[i][0] + ab[i][1]
            #print(time)
            #如果x次通关的最大时间小于x，那么直接输出x次通关的最大时间
            if time < x:
                return time
            #如果x次通关的最大时间大于x，那么需要计算x次通关的时间
            else:
                #先计算出x次通关的最小时间
                time = 0
                for i in range(n):
                    time += ab[i][0]
                #print(time)
                #如果x次通关的最小时间等于x，那么直接输出x次通关的最小时间
                if time == x:
                    return time
                #如果x次通关的最小时间小于x，那么需要计算x次通关的时间
                else:
                    #先计算出x次通关的最大时间
                    time = 0
                    for i in range(n):
                        time += ab[i][0] + ab[i][1]
                    #print(time)
                    #如果x次

=======
Suggestion 9

def solve():
    pass

=======
Suggestion 10

def func():
    return 0
