Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        ans = 0
        for a in A:
            if a % 2 == 1:
                ans += 1
        print(ans)

=======
Suggestion 2

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
Suggestion 3

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd = 0
        for a in A:
            if a % 2 == 1:
                odd += 1
        print(odd)

=======
Suggestion 4

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for i in range(len(A)):
            if A[i] % 2 != 0:
                count += 1
        print(count)

=======
Suggestion 5

def problems284_b():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(len([x for x in a if x % 2 == 1]))

=======
Suggestion 6

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        odd = 0
        for i in range(N):
            if A[i] % 2 == 1:
                odd += 1
        print(odd)

=======
Suggestion 7

def count_odd_numbers(n, numbers):
    count = 0
    for i in range(n):
        if numbers[i] % 2 != 0:
            count += 1
    return count

=======
Suggestion 8

def odd_numbers():
    '''
    Returns the number of odd numbers in a list of integers
    '''
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        print(len([x for x in A if x % 2 != 0]))

=======
Suggestion 9

def odd_number_count():
    input()
    return len(list(filter(lambda x: x%2 == 1, map(int, input().split()))))

=======
Suggestion 10

def get_input():
    test_cases = int(input())
    for test_case in range(test_cases):
        input()
        yield input().split()
