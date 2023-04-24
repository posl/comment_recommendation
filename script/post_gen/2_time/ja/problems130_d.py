Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while (right < N) and (total < K):
            total += A[right]
            right += 1
        if total < K:
            break
        ans += N - right + 1
        total -= A[left]
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total < K:
            break
        ans += N - right + 1
        total -= A[left]
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    tmp = 0
    for l in range(N):
        while r < N and tmp < K:
            tmp += A[r]
            r += 1
        if tmp >= K:
            ans += N - r + 1
        tmp -= A[l]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        s = 0
        for j in range(i, N):
            s += A[j]
            if s >= K:
                ans += N - j
                break

    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum >= K:
                count += N - j
                break
    print(count)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    left = 0
    right = 0
    sum = 0
    while left < N:
        while right < N and sum < K:
            sum += A[right]
            right += 1
        if sum >= K:
            ans += N - right + 1
        sum -= A[left]
        left += 1
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    l = 0
    r = 0
    ans = 0
    s = 0
    while l < n:
        while s < k and r < n:
            s += a[r]
            r += 1
        if s < k:
            break
        ans += n - r + 1
        s -= a[l]
        l += 1
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    ans = 0
    l = 0
    r = 0
    S = 0
    while l < N:
        while r < N and S < K:
            S += A[r]
            r += 1
        #print(l, r, S)
        if S >= K:
            ans += N - r + 1
        S -= A[l]
        l += 1
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    #累積和
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[i] + A[i])
    #print(sumA)
    #print(sumA[1:5])
    #print(sumA[2:5])
    #print(sumA[3:5])
    #print(sumA[4:5])
    #print(sumA[5:5])
    #print(sumA[6:5])
    #print(sumA[7:5])
    #print(sumA[8:5])
    #print(sumA[9:5])
    #print(sumA[10:5])
    #print(sumA[11:5])
    #print(sumA[12:5])
    #print(sumA[13:5])
    #print(sumA[14:5])
    #print(sumA[15:5])
    #print(sumA[16:5])
    #print(sumA[17:5])
    #print(sumA[18:5])
    #print(sumA[19:5])
    #print(sumA[20:5])
    #print(sumA[21:5])
    #print(sumA[22:5])
    #print(sumA[23:5])
    #print(sumA[24:5])
    #print(sumA[25:5])
    #print(sumA[26:5])
    #print(sumA[27:5])
    #print(sumA[28:5])
    #print(sumA[29:5])
    #print(sumA[30:5])
    #print(sumA[31:5])
    #print(sumA[32:5])
    #print(sumA[33:5])
    #print(sumA[34:5])
    #print(sumA[35:5])
    #print(sumA[36:5])
    #print(sumA[37:5])
    #print(sumA[38:5])
    #print(sumA[39:5])
    #print(sumA[40:5])
    #print(sumA[41:5])
    #print(sumA[42:5])
    #print(sumA[43:5

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    # 連続部分列の開始位置
    left = 0
    # 連続部分列の終了位置
    right = 0
    # 連続部分列の和
    sum = 0
    while True:
        # 連続部分列の和がK以上になるまで右端を伸ばす
        while right < N and sum < K:
            sum += A[right]
            right += 1
        # 連続部分列の和がK以上になったら、その時点での連続部分列の個数を加算し、左端を右にずらす
        if sum >= K:
            ans += N - right + 1
        # 左端を右にずらす
        sum -= A[left]
        left += 1
        # 左端がNに到達したら終了
        if left == N:
            break
    print(ans)

main()
