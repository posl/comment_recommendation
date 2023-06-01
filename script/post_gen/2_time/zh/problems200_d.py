Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def problems200_c():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    mod = [0] * 200
    for i in range(n):
        mod[a[i] % 200] += 1
    for i in range(200):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

problems200_c()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    B = [0]*200
    for i in range(N):
        B[A[i] % 200] += 1
    for i in range(200):
        ans += B[i]*(B[i]-1)//2
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    for i in range(n):
        if a[i] % 200 in d:
            d[a[i] % 200] += 1
        else:
            d[a[i] % 200] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2
    print(ans)

=======
Suggestion 5

def func():
    N = int(input())
    A = list(map(int, input().split()))
    # print(A)
    # print(len(A))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                count += 1
    print(count)

=======
Suggestion 6

def find_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]-nums[j])%200 == 0:
                count += 1
    return count

=======
Suggestion 7

def solve():
    print("solve")

=======
Suggestion 8

def count_pairs(n, a):
    d = {}
    for i in range(n):
        r = a[i] % 200
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    count = 0
    for k in d:
        if d[k] > 1:
            count += (d[k] - 1) * d[k] // 2
    return count

=======
Suggestion 9

def problems200_c():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)
    return

problems200_c()

=======
Suggestion 10

def get_count(a):
    a.sort()
    c = [0]*200
    for i in a:
        c[i%200] += 1
    count = 0
    for i in range(200):
        if c[i] > 1:
            count += c[i]*(c[i]-1)//2
    return count
