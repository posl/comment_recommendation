Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(2, 1001):
        cnt = 0
        for j in range(N):
            if A[j] % i == 0:
                cnt += 1
        if cnt > ans:
            ans = cnt
            ans_i = i
    print(ans_i)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    gcd = [0] * 1001
    for a in A:
        for i in range(2, a + 1):
            if a % i == 0:
                gcd[i] += 1
    print(gcd.index(max(gcd)))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_gcd = 0
    max_gcd_num = 0
    for i in range(2, A[-1]+1):
        gcd_num = 0
        for j in range(N):
            if A[j] % i == 0:
                gcd_num += 1
        if gcd_num >= max_gcd:
            max_gcd = gcd_num
            max_gcd_num = i
    print(max_gcd_num)

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    max_gcd = 0
    for k in range(2,1001):
        gcd = 0
        for i in range(n):
            if a[i] % k == 0:
                gcd += 1
        if max_gcd < gcd:
            max_gcd = gcd
            k_max_gcd = k
    print(k_max_gcd)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    max_gcd = 0
    max_num = 0
    for i in range(2, A[0] + 1):
        gcd_cnt = 0
        for j in range(N):
            if A[j] % i == 0:
                gcd_cnt += 1
        if gcd_cnt > max_gcd:
            max_gcd = gcd_cnt
            max_num = i
    print(max_num)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    #print(A)
    #print(A[0])
    for i in range(A[0],1,-1):
        #print(i)
        cnt = 0
        for j in range(N):
            if A[j] % i == 0:
                cnt += 1
        if cnt >= 2:
            print(i)
            return
    print(1)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A_max = A[0]
    A_max_gcd = 0
    for i in range(2, A_max+1):
        gcd = 0
        for j in range(N):
            if A[j] % i == 0:
                gcd += 1
        if gcd > A_max_gcd:
            A_max_gcd = gcd
            A_max_gcd_num = i
    print(A_max_gcd_num)
