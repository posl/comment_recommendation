Synthesizing 10/10 solutions

=======
Suggestion 1

def count_odd(list):
    count = 0
    for i in list:
        if i % 2 != 0:
            count += 1
    return count

=======
Suggestion 2

def problem284_b():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = input().split()
        count = 0
        for j in range(n):
            if int(a[j]) % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 3

def count_odd_number(a_list):
    count = 0
    for i in a_list:
        if i % 2 != 0:
            count += 1
    return count

=======
Suggestion 4

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for j in range(N):
            if A[j] % 2 != 0:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd = 0
        for j in range(N):
            if A[j] % 2 != 0:
                odd += 1
        print(odd)

=======
Suggestion 6

def test():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(sum([1 for a in A if a % 2 != 0]))

test()

=======
Suggestion 7

def count_odd(n, a):
    count = 0
    for i in range(n):
        if a[i] % 2 != 0:
            count += 1
    return count

=======
Suggestion 8

def main():
    num = int(input())
    for i in range(num):
        n = int(input())
        a_list = list(map(int, input().split()))
        count = 0
        for j in range(n):
            if a_list[j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 9

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0
        for j in range(n):
            if a[j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 10

def count_odd(n, a):
    count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            count += 1
    return count
