Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        if A[i] == B[i]:
            cnt1 += 1
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                cnt2 += 1
    print(cnt1)
    print(cnt2)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    count1 = 0
    count2 = 0
    for i in range(N):
        if A[i] == B[i]:
            count1 += 1
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] == B[j]:
                count2 += 1
    print(count1)
    print(count2//2)

=======
Suggestion 3

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

main()

=======
Suggestion 4

def solve(n, a, b):
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt1 += 1
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i] == b[j]:
                cnt2 += 1
    return (cnt1, cnt2//2)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_count = 0
    b_count = 0
    for i in range(n):
        if a[i] == b[i]:
            a_count += 1
            b_count += 1
        else:
            for j in range(n):
                if a[i] == b[j]:
                    b_count += 1
                    break
    print(a_count)
    print(b_count - a_count)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_index = {}
    b_index = {}
    for i in range(n):
        a_index[a[i]] = i
        b_index[b[i]] = i

    a_and_b = 0
    a_and_b_not_same_index = 0
    for i in range(1, n+1):
        if a_index[i] == b_index[i]:
            a_and_b += 1

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                if a_index[i] == b_index[j]:
                    a_and_b_not_same_index += 1

    print(a_and_b)
    print(a_and_b_not_same_index)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_set = set(a)
    b_set = set(b)
    
    count_1 = 0
    for i in range(n):
        if a[i] == b[i]:
            count_1 += 1
    
    count_2 = 0
    for i in range(n):
        if a[i] in b_set and a[i] != b[i]:
            count_2 += 1
    
    print(count_1)
    print(count_2)

=======
Suggestion 8

def func():
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

func()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_set = set(a)
    b_set = set(b)
    
    cnt_1 = 0
    cnt_2 = 0
    
    for i in range(n):
        if a[i] == b[i]:
            cnt_1 += 1
    
    for i in range(n):
        if a[i] != b[i]:
            if a[i] in b_set:
                cnt_2 += 1
            if b[i] in a_set:
                cnt_2 += 1
    
    print(cnt_1)
    print(cnt_2//2)
