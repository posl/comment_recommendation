Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count1 += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    for i in range(N):
        if A[i] == B[i]:
            ans1 += 1
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] == B[j]:
                    ans2 += 1
    print(ans1)
    print(ans2//2)
solve()

=======
Suggestion 3

def get_same_num(A, B):
    same_num = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            same_num += 1
    return same_num

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    set_a = set(a)
    set_b = set(b)
    print(len(set_a & set_b))
    print(len(set_a ^ set_b)))

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    res1 = 0
    res2 = 0
    for i in range(N):
        if A[i] == B[i]:
            res1 += 1
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                res2 += 1
    print(res1)
    print(res2)
    
solve()

=======
Suggestion 6

def count_same_position(n, a, b):
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1
    return count

=======
Suggestion 7

def get_same_num(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    return cnt

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt1 += 1
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                cnt2 += 1
    print(cnt1)
    print(cnt2)

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [i for i in range(1, n+1) if a[i-1] == b[i-1]]
    d = [i for i in range(1, n+1) if a[i-1] in b and a[i-1] != b[i-1]]
    print(len(c))
    print(len(d))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] == b[i]:
            count1 += 1
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i] == b[j]:
                    count2 += 1
    print(count1)
    print(count2//2)
