Synthesizing 10/10 solutions

=======
Suggestion 1

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
    for j in range(n):
        for k in range(n):
            if j != k and a[j] == b[k]:
                d += 1
    print(c)
    print(d)

=======
Suggestion 3

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
            if a[i] == b[j] and i != j:
                ans2 += 1
    print(ans1)
    print(ans2)

=======
Suggestion 4

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
            if a[i] == b[j] and i != j:
                cnt2 += 1

    print(cnt1)
    print(int(cnt2/2))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1
    print(count)
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[j] and i != j:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = 0
    for i in range(n):
        if a[i] == b[i]:
            c += 1

    d = 0
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                d += 1

    print(c)
    print(d)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1

    b_dict = {}
    for i in range(n):
        b_dict[b[i]] = i

    count2 = 0
    for i in range(n):
        if a[i] in b_dict and b_dict[a[i]] != i:
            count2 += 1

    print(count)
    print(count2)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_dict = {}
    b_dict = {}

    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i

    a_set = set(a)
    b_set = set(b)

    a_b_same = a_set & b_set
    a_b_diff = a_set ^ b_set

    same = 0
    diff = 0

    for i in a_b_same:
        if a_dict[i] == b_dict[i]:
            same += 1
        else:
            diff += 1

    print(same)
    print(diff)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_set = set(a)
    b_set = set(b)

    same = 0
    diff = 0

    for i in range(n):
        if a[i] == b[i]:
            same += 1
        elif a[i] in b_set:
            diff += 1

    print(same)
    print(diff)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(len(set(A) & set(B)))
    print(len(set(A) & set(B, i != j)))
