Synthesizing 10/10 solutions

=======
Suggestion 1

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
        if a[i] in b and a[i] != b[i]:
            d += 1
    print(c)
    print(d)

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
            if a[i] == b[j] and i != j:
                d += 1
    print(c)
    print(d)

=======
Suggestion 3

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
            if a[i] == b[j] and i != j:
                count2 += 1

    print(count1)
    print(count2)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1

    A_set = set(A)
    B_set = set(B)
    C_set = A_set & B_set

    print(count)
    print(len(C_set) - count)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
        else:
            for j in range(n):
                if a[i] == b[j]:
                    ans2 += 1

    print(ans1)
    print(ans2)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans1 = 0
    ans2 = 0

    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1

    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                ans2 += 1

    print(ans1)
    print(ans2)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    same = 0
    diff = 0

    for i in range(n):
        if a[i] == b[i]:
            same += 1

    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                diff += 1

    print(same)
    print(diff)

=======
Suggestion 8

def solve():
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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_b = 0
    b_b = 0
    for i in range(n):
        if a[i] == b[i]:
            a_b += 1

    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                b_b += 1

    print(a_b)
    print(b_b)

=======
Suggestion 10

def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #compute
    a_b = 0
    b_b = 0
    for i in range(n):
        if a[i] == b[i]:
            a_b += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                b_b += 1

    #output
    print(a_b)
    print(b_b)
