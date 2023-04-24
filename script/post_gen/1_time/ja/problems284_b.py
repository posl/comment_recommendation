Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for j in range(N):
            if A[j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 2

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for a in A:
            if a % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 3

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        odd = 0
        for j in range(n):
            if a[j] % 2 == 1:
                odd += 1
        print(odd)

=======
Suggestion 4

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(sum([1 for a in A if a % 2 == 1]))

=======
Suggestion 5

def odd_number():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd = 0
        for j in range(N):
            if A[j] % 2 == 1:
                odd += 1
        print(odd)

=======
Suggestion 6

def get_odd_num(num_list):
    odd_num = 0
    for i in num_list:
        if i % 2 != 0:
            odd_num += 1
    return odd_num

test_num = int(input())
for i in range(test_num):
    num = int(input())
    num_list = list(map(int, input().split()))
    print(get_odd_num(num_list))

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(sum([i % 2 for i in A]))
