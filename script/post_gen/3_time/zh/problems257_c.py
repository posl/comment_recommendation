Synthesizing 10/10 solutions

=======
Suggestion 1

def isChild(num, weight, s):
    i = 0
    for i in range(len(s)):
        if s[i] == '0':
            if weight[i] >= num:
                return False
        else:
            if weight[i] < num:
                return False
    return True

=======
Suggestion 2

def main():
    N=int(input())
    S=input()
    W=list(map(int,input().split()))
    max=0
    for i in range(0,N):
        if S[i]=='1':
            if max<W[i]:
                max=W[i]
    print(max)
main()

=======
Suggestion 3

def f(x):
    y = 0
    for i in range(N):
        if S[i] == "0" and x > W[i]:
            y += 1
        elif S[i] == "1" and x <= W[i]:
            y += 1
    return y

N = int(input())
S = input()
W = list(map(int, input().split()))
l = 0
r = 10 ** 9 + 1
while l + 1 < r:
    m = (l + r) // 2
    if f(m) == N:
        l = m
    else:
        r = m
print(l)

=======
Suggestion 4

def func(n, s, w):
    # 1. 二分查找
    # 2. 计算每一个X对应的f(x)
    # 3. 找到最大的f(x)
    # 4. 找到最大的f(x)对应的X
    # 5. 打印最大的f(x)
    start = 1
    end = max(w)
    while start <= end:
        mid = (start + end) // 2
        # print("start = {}, end = {}, mid = {}".format(start, end, mid))
        if f(mid, n, s, w):
            start = mid + 1
        else:
            end = mid - 1
    print(start - 1)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    #print(n, s, w)
    s = list(s)
    #print(s)
    #print(w)

    # 二分法
    def func(x):
        res = 0
        for i in range(n):
            if s[i] == '1':
                if w[i] >= x:
                    res += 1
            else:
                if w[i] < x:
                    res += 1
        return res

    l = 0
    r = 10 ** 9 + 1
    while r - l > 1:
        mid = (l + r) // 2
        if func(mid) >= n // 2 + 1:
            l = mid
        else:
            r = mid
    print(l)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    s = [int(i) for i in s]
    s1 = [0] * n
    s2 = [0] * n
    for i in range(n):
        if s[i] == 0:
            s1[i] = w[i]
        else:
            s2[i] = w[i]
    s1.sort()
    s2.sort()
    for i in range(n - 1):
        s1[i + 1] += s1[i]
        s2[i + 1] += s2[i]
    ans = 0
    for i in range(n + 1):
        if i < n:
            ans = max(ans, s1[i])
        if i > 0:
            ans = max(ans, s2[i - 1])
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    #print(n, s, w)
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 3
    #s = "000"
    #w = [1, 2, 3]
    #s = "10101"
    #w = [60, 45, 30, 40, 80]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]

    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]
    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]

    #n = 5
    #s = "10101"
    #w = [60, 50, 50, 50, 60]

    #n =

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    left = 0
    right = 10**9+1
    while right - left > 1:
        mid = (left + right) // 2
        ok = True
        for i in range(N):
            if S[i] == '0' and W[i] >= mid:
                ok = False
        if ok:
            left = mid
        else:
            right = mid
    print(left)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    child = []
    adult = []
    for i in range(n):
        if s[i] == '0':
            child.append(w[i])
        else:
            adult.append(w[i])
    child.sort()
    adult.sort()
    ch = len(child)
    ad = len(adult)
    if ad == 0:
        print(ch)
        exit()
    if ch == 0:
        print(0)
        exit()
    ans = 0
    for i in range(1, ch+1):
        if i > ad:
            break
        ans = max(ans, sum(child[:ch-i])+sum(adult[:i]))
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N, S, W)
    #print(S[1])
    #print(W[1])
    #print(len(S))
    #print(len(W))
    #print(S[0], S[1], S[2], S[3], S[4])
    #print(W[0], W[1], W[2], W[3], W[4])
    #print(S[0:1], S[1:2], S[2:3], S[3:4], S[4:5])
    #print(W[0:1], W[1:2], W[2:3], W[3:4], W[4:5])
    #print(S[0:2], S[1:3], S[2:4], S[3:5])
    #print(W[0:2], W[1:3], W[2:4], W[3:5])
    #print(S[0:3], S[1:4], S[2:5])
    #print(W[0:3], W[1:4], W[2:5])
    #print(S[0:4], S[1:5])
    #print(W[0:4], W[1:5])
    #print(S[0:5])
    #print(W[0:5])
    #print(S[0:1], S[1:2], S[2:3], S[3:4], S[4:5])
    #print(W[0:1], W[1:2], W[2:3], W[3:4], W[4:5])
    #print(S[0:2], S[1:3], S[2:4], S[3:5])
    #print(W[0:2], W[1:3], W[2:4], W[3:5])
    #print(S[0:3], S[1:4], S[2:5])
    #print(W[0:3], W[1:4], W[2:5])
    #print(S[0:4], S[1:5])
    #print(W[0:4
