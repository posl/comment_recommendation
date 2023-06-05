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
        elif a[i] in b:
            count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 2

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
Suggestion 3

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
            if i != j and A[i] == B[j]:
                count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1
    print(count)
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = set(a) & set(b)
    print(len(s))

    d = {x: 0 for x in s}
    for x in a:
        d[x] += 1
    for x in b:
        d[x] += 1

    print(sum([1 for x in d if d[x] > 1]))

=======
Suggestion 6

def readinput():
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    return n,A,B

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_set = set(a)
    b_set = set(b)

    a_b_same = a_set & b_set
    a_b_diff = a_set ^ b_set

    a_b_same_num = 0
    a_b_diff_num = 0

    for i in range(n):
        if a[i] in a_b_same and b[i] in a_b_same:
            a_b_same_num += 1
        if a[i] in a_b_diff or b[i] in a_b_diff:
            a_b_diff_num += 1

    print(a_b_same_num)
    print(a_b_diff_num)

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
    count_1 = 0
    count_2 = 0
    for i in range(n):
        if a[i] in b_dict.keys() and a[i] == b[i]:
            count_1 += 1
        if a[i] in b_dict.keys() and a[i] != b[i]:
            count_2 += 1
    print(count_1)
    print(count_2)

=======
Suggestion 9

def get_same_num(A, B):
    same_num = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            same_num += 1
    return same_num

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
            if i != j and a[i] == b[j]:
                count2 += 1
    print(count1)
    print(count2)
