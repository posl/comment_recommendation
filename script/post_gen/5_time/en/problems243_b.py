Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
    for i in range(N):
        for j in range(N):
            if A[i] == B[j] and i != j:
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
    for i in a:
        if i in b:
            d += 1
    print(c)
    print(d-c)

=======
Suggestion 3

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
        if a[i] in b and a[i] != b[i]:
            cnt2 += 1
    print(cnt1)
    print(cnt2)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
        else:
            if A[i] in B:
                count2 += 1

    print(count1)
    print(count2)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count_1 = 0
    count_2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count_1 += 1
    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] == B[j]:
                    count_2 += 1
    print(count_1)
    print(count_2)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt += 1
    print(cnt)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    same = 0
    diff = 0
    for i in range(N):
        if A[i] == B[i]:
            same += 1
        else:
            for j in range(N):
                if A[i] == B[j]:
                    diff += 1
                    break

    print(same)
    print(diff)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
        for j in range(n):
            if i != j and a[i] == b[j]:
                ans2 += 1
    print(ans1)
    print(ans2)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_dict = {a[i]: i for i in range(n)}
    b_dict = {b[i]: i for i in range(n)}

    a_b = set(a_dict.keys()) & set(b_dict.keys())
    a_b_same = set([i for i in a_dict.keys() if i in b_dict.keys() and a_dict[i] == b_dict[i]])
    a_b_diff = a_b - a_b_same

    print(len(a_b_same))
    print(len(a_b_diff))

=======
Suggestion 10

def read_int():
    return int(input())
