Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt1 += 1
        for j in range(n):
            if a[i] == b[j]:
                cnt2 += 1

    print(cnt1)
    print(cnt2 - cnt1)

=======
Suggestion 2

def get_same_num(a, b):
    return len(set(a) & set(b))

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
        for j in range(n):
            if i != j and a[i] == b[j]:
                cnt2 += 1
    print(cnt1)
    print(cnt2)

=======
Suggestion 4

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

=======
Suggestion 5

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
Suggestion 6

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

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = 0
    d = 0
    for i in range(n):
        if a[i] == b[i]:
            c += 1
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i] == b[j]:
                    d += 1
    print(c)
    print(d // 2)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
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

=======
Suggestion 9

def main():
    n = int(input())
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    c = [i for i in a if i in b]
    print(len(c))
    d = [i for i in a if i not in b]
    e = [i for i in b if i not in a]
    print(len(d)+len(e))
