Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #A = [1,1,2,1,2]
    #N = 5
    #A = [1,2,3,4]
    #N = 4
    #A = [3,3,3,3,3]
    #N = 5
    #A = [1,2,1,4,2,1,4,1]
    #N = 8
    #A = [1,2,1,4,2,1,4,1,1,1,1,1,1,1,1,1]
    #N = 16
    
    #print(A)
    #print(N)
    #print()
    
    #print(A)
    #print()
    #print(N)
    #print()
    
    #print(A)
    #print(N)
    #print()
    
    #

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    from collections import defaultdict
    d = defaultdict(int)

    for a in A:
        d[a] += 1

    ans = []
    for a in A:
        ans.append(N-1 - (d[a]-1))
    print(*ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count_list = [0] * N
    for i in range(N):
        count_list[A[i]-1] += 1
    total = 0
    for i in range(N):
        total += count_list[i] * (count_list[i]-1) // 2
    for i in range(N):
        print(total - (count_list[A[i]-1]-1))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1

    total = 0
    for i in range(N):
        total += d[A[i]] - 1

    for i in range(N):
        print(total - (d[A[i]] - 1))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    #print(N)
    #print(A)
    #print("ok")
    #print(A)
    #print(A.count(1))
    #print(A.count(2))
    #print(A.count(3))
    #print(A.count(4))
    #print(A.count(5))
    #print(A.count(6))
    #print(A.count(7))
    #print(A.count(8))
    #print(A.count(9))
    #print(A.count(10))
    #print(A.count(11))
    #print(A.count(12))
    #print(A.count(13))
    #print(A.count(14))
    #print(A.count(15))
    #print(A.count(16))
    #print(A.count(17))
    #print(A.count(18))
    #print(A.count(19))
    #print(A.count(20))
    #print(A.count(21))
    #print(A.count(22))
    #print(A.count(23))
    #print(A.count(24))
    #print(A.count(25))
    #print(A.count(26))
    #print(A.count(27))
    #print(A.count(28))
    #print(A.count(29))
    #print(A.count(30))
    #print(A.count(31))
    #print(A.count(32))
    #print(A.count(33))
    #print(A.count(34))
    #print(A.count(35))
    #print(A.count(36))
    #print(A.count(37))
    #print(A.count(38))
    #print(A.count(39))
    #print(A.count(40))
    #print(A.count(41))
    #print(A.count(42))
    #print(A.count(43))
    #print(A.count(44))
    #print(A.count(45))
    #print(A.count(46))
    #print(A.count(47))
    #print(A.count(48))
    #print(A.count(49))
    #print(A.count(50))
    #print(A.count(51))
    #print(A.count(52))
    #print(A.count(53))
    #print(A.count(54))
    #print(A.count(55))
    #print(A.count(56))
    #print(A.count(57))
    #print(A.count

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_set = set(A)
    A_len = len(A)
    ans = [0] * N
    for num in A_set:
        tmp = A.count(num)
        ans[num-1] = tmp * (tmp-1) // 2
    for i in range(A_len):
        print(ans[A[i]-1])

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    a.append(-1)
    ans = [0 for _ in range(n)]
    count = 1
    for i in range(n):
        if a[i] == a[i+1]:
            count += 1
        else:
            ans[a[i]-1] = count
            count = 1
    for i in range(n):
        print(n-ans[i])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * N
    for i in range(N):
        B[A[i]-1] += 1
    #print(B)
    ans = 0
    for i in range(N):
        ans += B[i] * (B[i]-1) // 2
    #print(ans)
    for i in range(N):
        print(ans - B[A[i]-1] + 1)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    d = {}

    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    ans = 0
    for i in d:
        ans += d[i] * (d[i] - 1) // 2

    for i in a:
        print(ans - (d[i] - 1))

=======
Suggestion 10

def make_counter(N):
    counter = [0] * (N + 1)
    return counter
