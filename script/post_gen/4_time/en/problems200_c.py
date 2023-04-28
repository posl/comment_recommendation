Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                count += 1
    print(count)
    return 0

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200
    for i in range(N):
        B[A[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += B[i] * (B[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = [0] * 200
    for i in a:
        m[i % 200] += 1
    ans = 0
    for i in m:
        ans += i * (i - 1) // 2
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] - a[j]) % 200 == 0:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_mod = [a % 200 for a in A]
    A_mod_count = [0] * 200
    for a_mod in A_mod:
        A_mod_count[a_mod] += 1
    count = 0
    for i in range(200):
        count += A_mod_count[i] * (A_mod_count[i] - 1) // 2
    print(count)

=======
Suggestion 7

def problems200_c():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i % 200 for i in a]
    a.sort()
    ans = 0
    cnt = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            cnt += 1
        else:
            ans += (cnt * (cnt - 1)) // 2
            cnt = 1
    ans += (cnt * (cnt - 1)) // 2
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = [x%200 for x in a]
    a.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] == a[j]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    #print(len(A))

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    #print(n)
    #print(a)

    #a.sort()
    #print(a)
    #print(len(a))

    #for i in range(len(a)):
    #    print(a[i])

    #for i in range(len(a)):
    #    for j in range(len(a)):
    #        print(a[i], a[j])

    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i < j and (a[i] - a[j]) % 200 == 0:
                count += 1
                #print(a[i], a[j])

    print(count)
