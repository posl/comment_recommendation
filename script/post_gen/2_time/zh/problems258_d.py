Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0]+x[1])
    #print(ab)
    ans = 0
    for i in range(n):
        if x >= ab[i][0]+ab[i][1]:
            ans += ab[i][0]+ab[i][1]
            x -= ab[i][0]+ab[i][1]
        else:
            ans += x
            x = 0
    print(ans)

=======
Suggestion 2

def get_min_time(n, x, a_list, b_list):
    min_time = 0
    for i in range(n):
        if i == 0:
            min_time += a_list[i] + b_list[i]
        else:
            min_time += a_list[i]
    return min_time

=======
Suggestion 3

def solve(N, X, AB):
    A = []
    B = []
    for i in range(N):
        A.append(AB[i][0])
        B.append(AB[i][1])
    #print(N, X, A, B)
    min_time = 10 ** 18
    for i in range(N):
        time = A[i]
        count = 1
        j = i - 1
        while j >= 0:
            time += B[j]
            count += 1
            j -= 1
        time += B[i] * ((X - count) // N)
        count += N * ((X - count) // N)
        j = 0
        while count < X:
            time += B[j]
            count += 1
            j += 1
        min_time = min(min_time, time)
    return min_time

=======
Suggestion 4

def solve():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for a, b in AB:
        ans += a
        if ans > X:
            print(-1)
            return
        ans += b
    print(ans)

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    min_time = 1000000000000000000
    for i in range(n):
        time = 0
        for j in range(n):
            time += a[j] + b[j]
        if time < min_time:
            min_time = time
    print(min_time)

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    res = 0
    for i in range(n):
        res += a[i] + b[i]
    if res <= x:
        print(res)
    else:
        res = 0
        for i in range(n):
            res += a[i]
            if res > x:
                print(i)
                return
        print(n)

main()

=======
Suggestion 7

def solve():
    pass

=======
Suggestion 8

def solve():
    N,X=list(map(int,input().split()))
    AB=[list(map(int,input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[1])
    ans=0
    for a,b in AB:
        ans+=a+b
    ans*=X
    ans-=AB[-1][1]
    print(ans)

=======
Suggestion 9

def main():
    # 读入数据
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # 二分查找
    left = 0
    right = 10 ** 18
    while right - left > 1:
        mid = (left + right) // 2
        # 判断mid分钟内能否清除x个阶段
        cnt = 0
        for i in range(n):
            # 如果mid分钟内能清除第i个阶段
            if a[i] <= mid:
                cnt += (mid - a[i]) // b[i] + 1
        if cnt >= x:
            right = mid
        else:
            left = mid
    print(right)

=======
Suggestion 10

def solve():
    N,X = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    ans = 0
    for i in range(N):
        ans += A[i]*B[i]
    ans += min(B)
    for i in range(N):
        ans += (X-1)*min(A[i],B[i])
    return ans

print(solve())
