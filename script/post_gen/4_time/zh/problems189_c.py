Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #输入
    N = int(input())
    A = list(map(int, input().split()))

    #计算
    max_orange = 0
    for l in range(N):
        for r in range(l, N):
            x = min(A[l:r+1])
            max_orange = max(max_orange, x*(r-l+1))

    #输出
    print(max_orange)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_a_index = a.index(max_a)
    max_a_count = a.count(max_a)
    max_a_count_index = max_a_index + max_a_count - 1
    if max_a_index == 0:
        max_a_count_left = 0
    else:
        max_a_count_left = a[:max_a_index].count(max_a)
    if max_a_count_index == n - 1:
        max_a_count_right = 0
    else:
        max_a_count_right = a[max_a_count_index + 1:].count(max_a)

    if max_a_count_left + max_a_count_right == max_a_count:
        print(max_a * max_a_count)
        return

    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = min(a[i:j + 1])
            ans = max(ans, x * (j + 1 - i))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))

    print(ans)

=======
Suggestion 5

def max_orange(N, A):
    max_orange = 0
    for l in range(1, N+1):
        for r in range(l, N+1):
            for x in range(1, max(A[l-1:r])):
                if x <= A[l-1:r].min():
                    max_orange = max(max_orange, x*(r-l+1))
    return max_orange

N = 6
A = [2, 4, 4, 9, 4, 9]
print(max_orange(N, A))

N = 6
A = [200, 4, 4, 9, 4, 9]
print(max_orange(N, A))

=======
Suggestion 6

def get_max_orange(orange_list):
    max_orange = 0
    for i in range(len(orange_list)):
        for j in range(i, len(orange_list)):
            for k in range(1, orange_list[j]+1):
                if max_orange < k * (j-i+1):
                    max_orange = k * (j-i+1)
    return max_orange

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    for l in range(N):
        for r in range(l, N):
            x = min(A[l:r+1])
            if max < x * (r-l+1):
                max = x * (r-l+1)
    print(max)

=======
Suggestion 8

def solve(n, a):
    max_a = max(a)
    ans = 0
    for x in range(1, max_a + 1):
        for l in range(n):
            for r in range(l, n):
                cnt = 0
                for i in range(l, r + 1):
                    if a[i] >= x:
                        cnt += x
                ans = max(ans, cnt)
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 9

def solve(N, A):
    max_A = max(A)
    max_A_index = A.index(max_A)
    max_A_r = A[max_A_index:]
    max_A_l = A[:max_A_index + 1]
    max_A_l.reverse()
    max_A_l_index = max_A_l.index(max_A)
    max_A_r_index = max_A_r.index(max_A)
    return max_A * (max_A_l_index + max_A_r_index + 1)

=======
Suggestion 10

def solve(n, a):
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x * (r - l + 1))
    return ans

n = int(input())
a = [int(i) for i in input().split()]
print(solve(n, a))
