Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        ans += a - 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(N * max(A) - sum(A))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = sum(A) - N
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A) - N)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([a - 1 for a in A]))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a)-n)

=======
Suggestion 7

def main():
    N = int(input())
    As = list(map(int, input().split()))
    mod = [0] * (10**5 + 1)
    for a in As:
        for i in range(1, a):
            mod[i] += 1
    ans = 0
    for i in range(1, 10**5 + 1):
        if mod[i] == N:
            ans += i
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    max_a = a_list[-1]
    a_list.pop()
    a_list.reverse()
    max_sum = 0
    for i in range(n-1):
        max_sum += max_a % a_list[i]
    print(max_sum)
