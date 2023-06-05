Synthesizing 10/10 solutions

=======
Suggestion 1

def problems170_d():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [True] * n
    for i in range(n):
        if b[i]:
            for j in range(i + 1, n):
                if a[j] % a[i] == 0:
                    b[j] = False
    print(sum(b))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i + 1]:
                count += 1
        elif i == N - 1:
            if A[i] != A[i - 1]:
                count += 1
        else:
            if A[i] != A[i - 1] and A[i] != A[i + 1]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 1
    for i in range(1, n):
        if arr[i] % arr[ans - 1] != 0:
            arr[ans] = arr[i]
            ans += 1
    print(ans)

=======
Suggestion 4

def solve(N, A):
    # 1. 从小到大排序
    A.sort()
    # 2. 从小到大累加
    # 3. 按照条件减去
    ans = 0
    for i in range(N):
        ans += i
        if i > 0 and A[i] == A[i - 1]:
            ans -= 1
    return ans

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
a.sort()
b = [0] * n
for i in range(n):
    b[i] = gcd(b[i-1], a[i])
c = [0] * n
for i in range(n):
    c[i] = gcd(c[i-1], a[n-i-1])
ans = 0
for i in range(n):
    if i == 0:
        if c[n-i-2] % a[n-i-1] == 0:
            ans += 1
    elif i == n-1:
        if b[i-1] % a[i] == 0:
            ans += 1
    else:
        if b[i-1] % a[i] == 0 and c[n-i-2] % a[n-i-1] == 0:
            ans += 1
print(ans)

=======
Suggestion 6

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                count += 1
        elif i == N-1:
            if A[i-1] != A[i]:
                count += 1
        elif A[i-1] != A[i] and A[i] != A[i+1]:
            count += 1
    print(count)

=======
Suggestion 8

def get_list_from_line():
    return [int(x) for x in input().split()]

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0 or a[i] != a[i - 1]:
            ok = True
            for j in range(i + 1, n):
                if a[j] % a[i] == 0:
                    ok = False
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 10

def func1():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        flag = True
        for j in range(n):
            if i != j and a[j] % a[i] == 0:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
