Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    print("243_b")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    d = 0
    for i in range(n):
        if a[i] == b[i]:
            c += 1
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                d += 1
    print(c)
    print(d)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #print(n, a, b)
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i] == b[j]:
                    ans2 += 1
    print(ans1)
    print(ans2//2)

=======
Suggestion 4

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(n):
        if A[i] == B[i]:
            count1 += 1
    for i in range(n):
        for j in range(n):
            if A[i] == B[j] and i != j:
                count2 += 1
    print(count1)
    print(count2//2)

=======
Suggestion 5

def solve1():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res1 = 0
    res2 = 0
    for i in range(n):
        if a[i] == b[i]:
            res1 += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                res2 += 1
    print(res1)
    print(res2//2)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    d = 0
    for i in range(n):
        if a[i] == b[i]:
            c += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                d += 1
    print(c)
    print(d)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    count_a = 0
    count_b = 0
    for i in range(N):
        if A[i] == B[i]:
            count_a += 1
    print(count_a)

    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] == B[j]:
                    count_b += 1
    print(count_b//2)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if a[i]==b[i]:
            cnt1 += 1
    for i in range(n):
        for j in range(n):
            if a[i]==b[j] and i!=j:
                cnt2 += 1
    print(cnt1)
    print(cnt2//2)

=======
Suggestion 9

def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    #compute
    #1.
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1
    print(count)
    
    #2.
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count += 1
    print(count)
