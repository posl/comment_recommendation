Synthesizing 10/10 solutions

=======
Suggestion 1

def d170():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if i == 0:
            if a[i] != a[i+1]:
                count += 1
        elif i == n-1:
            if a[i] != a[i-1]:
                count += 1
        elif a[i] != a[i-1] and a[i] != a[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def get_divisor(num):
    divisor_list = []
    for i in range(1, num+1):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    #print(A)
    #print(N)
    #print(A[N-1])
    #print(A[N-2])
    #print(A[N-3])
    #print(A[N-4])
    #print(A[N-5])

    count = 0
    for i in range(N-1):
        if A[i] != A[i+1]:
            count += 1
    if A[N-1] != A[N-2]:
        count += 1
    print(count)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(10**6+1)
    ans = 0
    for i in range(n):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    max = A[-1]
    is_div = [0] * (max + 1)
    for i in range(N):
        is_div[A[i]] = 1
    for i in range(1, max+1):
        if is_div[i] == 0:
            continue
        for j in range(2*i, max+1, i):
            is_div[j] = 0
    print(sum(is_div))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i != j and a[j] % a[i] == 0:
                break
        else:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def solve():
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
                    break
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0 or A[i] != A[i - 1]:
            ok = True
            for j in range(i + 1, N):
                if A[j] % A[i] == 0:
                    ok = False
                    break
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    cnt = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                cnt += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                cnt += 1
        else:
            if A[i-1] != A[i] and A[i] != A[i+1]:
                cnt += 1
    print(cnt)
