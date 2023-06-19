Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in a:
        if i % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(n):
        a = int(input())
        b = list(map(int, input().split()))
        count = 0
        for j in b:
            if j % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 3

def read_int():
    return int(input())

=======
Suggestion 4

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0
        for j in range(n):
            if a[j] % 2 != 0:
                count += 1
        print(count)

main()

=======
Suggestion 5

def get_input():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        yield (N, A)

=======
Suggestion 6

def is_odd(x):
    if x % 2 == 0:
        return False
    else:
        return True

=======
Suggestion 7

def count_odd(nums):
    count = 0
    for i in nums:
        if i % 2 != 0:
            count += 1
    return count

=======
Suggestion 8

def main():
    n = int(input())
    for i in range(n):
        a = int(input())
        b = input().split()
        b = list(map(int, b))
        count = 0
        for j in range(a):
            if b[j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(n):
        a = int(input())
        b = list(map(int, input().split()))
        count = 0
        for j in b:
            if j % 2 == 1:
                count += 1
        print(count)

main()

=======
Suggestion 10

def count_odd_num(num_list):
    count = 0
    for i in num_list:
        if i % 2 != 0:
            count += 1
    return count
