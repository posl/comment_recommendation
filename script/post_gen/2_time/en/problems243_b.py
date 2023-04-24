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
    A.sort()
    B.sort()
    for i in range(N):
        if A[i] in B:
            count2 += 1
    print(count1)
    print(count2 - count1)

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    same_pos = 0
    diff_pos = 0
    for i in range(n):
        if a[i] in b_dict:
            if a_dict[a[i]] == b_dict[a[i]]:
                same_pos += 1
            else:
                diff_pos += 1
    print(same_pos)
    print(diff_pos)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    same = 0
    diff = 0
    for i in range(n):
        if a[i] in b_dict.keys():
            if a_dict[a[i]] == b_dict[a[i]]:
                same += 1
            else:
                diff += 1
    print(same)
    print(diff)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_dict = dict()
    B_dict = dict()
    for i in range(N):
        A_dict[A[i]] = i
        B_dict[B[i]] = i
    same = 0
    diff = 0
    for i in range(N):
        if A[i] in B_dict:
            if i == B_dict[A[i]]:
                same += 1
            else:
                diff += 1
    print(same)
    print(diff)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    c = 0
    d = 0
    while i < n and j < n:
        if a[i] == b[j]:
            c += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    i = 0
    j = 0
    while i < n and j < n:
        if a[i] == b[j]:
            if i != j:
                d += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(c)
    print(d)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                count += 1
                break
    print(count)
    print(count - n)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = {A[i]: i for i in range(N)}
    B = {B[i]: i for i in range(N)}
    same = 0
    diff = 0
    for a in A:
        if a in B:
            if A[a] == B[a]:
                same += 1
            else:
                diff += 1
    print(same)
    print(diff)

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a2b = {}
    for i in range(N):
        a2b[A[i]] = B[i]
    a2i = {}
    for i in range(N):
        a2i[A[i]] = i
    b2i = {}
    for i in range(N):
        b2i[B[i]] = i
    same = 0
    diff = 0
    for i in range(N):
        if A[i] == B[i]:
            same += 1
        else:
            if a2i[B[i]] == b2i[A[i]]:
                diff += 1
    print(same)
    print(diff)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(zip(A, B))
    A_set = set(A)
    B_set = set(B)
    print(len(A_set & B_set))
    print(len(C) - len(A_set | B_set))
