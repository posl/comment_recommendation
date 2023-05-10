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
            if A[i] == B[j]:
                count2 += 1

    count2 -= count1
    count2 //= 2

    print(count1)
    print(count2)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i+1
        b_dict[b[i]] = i+1

    a_set = set(a)
    b_set = set(b)
    a_and_b = a_set & b_set

    a_and_b_dict = {}
    for x in a_and_b:
        a_and_b_dict[x] = [a_dict[x], b_dict[x]]

    cnt1 = 0
    cnt2 = 0
    for x in a_and_b_dict:
        if a_and_b_dict[x][0] == a_and_b_dict[x][1]:
            cnt1 += 1
        else:
            cnt2 += 1
    print(cnt1)
    print(cnt2)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    a = 0
    b = 0
    for i in range(N):
        if A[i] == B[i]:
            a += 1

        for j in range(N):
            if i != j and A[i] == B[j]:
                b += 1
    print(a)
    print(b)

=======
Suggestion 4

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
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    a_and_b = 0
    a_and_b_diff = 0

    for i in range(n):
        if a[i] == b[i]:
            a_and_b += 1
        else:
            for j in range(n):
                if a[i] == b[j]:
                    a_and_b_diff += 1
                    break

    print(a_and_b)
    print(a_and_b_diff)

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
            if i != j and a[i] == b[j]:
                count2 += 1
    print(count1)
    print(count2)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dict = {}
    for i in range(n):
        dict[a[i]] = i
    dict2 = {}
    for i in range(n):
        dict2[b[i]] = i
    
    count1 = 0
    for i in range(n):
        if a[i] in b:
            count1 += 1
    
    count2 = 0
    for i in range(n):
        if a[i] in b and dict[a[i]] != dict2[a[i]]:
            count2 += 1
    
    print(count1)
    print(count2)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans_1 = 0
    ans_2 = 0
    for i in range(N):
        if A[i] == B[i]:
            ans_1 += 1
    for i in range(N):
        for j in range(N):
            if A[i] == B[j]:
                ans_2 += 1
    print(ans_1)
    print(ans_2-ans_1)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_b = 0
    for i in range(n):
        if a[i] == b[i]:
            a_b += 1
    a_b2 = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                a_b2 += 1
    print(a_b)
    print(a_b2-a_b)

=======
Suggestion 10

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
            if a[i] == b[j]:
                d += 1
    print(c)
    print(d-c)
