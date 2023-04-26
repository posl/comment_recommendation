Synthesizing 10/10 solutions

=======
Suggestion 1

def f(m):
    res = 0
    for i in range(N):
        res += m % a[i]
    return res

N = int(input())
a = list(map(int, input().split()))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        ans += i - 1
    print(ans)

=======
Suggestion 3

def f(m):
    sum = 0
    for i in range(N):
        sum += m % a[i]
    return sum

N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

l = 0
r = a[0] * (N - 1)
while r - l > 1:
    m = (l + r) // 2
    if f(m) >= f(m + 1):
        r = m
    else:
        l = m

print(f(r))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * i
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.reverse()
    f = [0] * N
    f[0] = a[0]
    for i in range(1, N):
        f[i] = f[i - 1] + a[i]
    print(f[N - 1])

=======
Suggestion 6

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)
    max_list = []
    for i in range(n):
        max_list.append(a_list[i]*(n-i))
    print(max(max_list))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 二分探索
    left = 0
    right = 10 ** 5 + 1
    while right - left > 1:
        mid = (left + right) // 2
        # 二分探索の条件
        if is_ok(a, mid):
            right = mid
        else:
            left = mid
    print(right)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    a.sort()
    #print(a)
    max_a = a[n-1]
    #print(max_a)
    sum = 0
    for i in range(1, max_a+1):
        sum_tmp = 0
        for j in range(0, n):
            sum_tmp += i % a[j]
            #print(sum_tmp)
        if sum_tmp > sum:
            sum = sum_tmp
            #print(sum)
    print(sum)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    a.remove(max_a)
    a.append(max_a-1)
    print(sum(a))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max = A[-1]
    B = [0] * (max + 1)
    for i in range(N):
        for j in range(A[i], max + 1, A[i]):
            B[j] += 1
    ans = 0
    for i in range(max + 1):
        ans += B[i] * i
    print(ans)
