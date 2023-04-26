Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1/a[i]
    print(1/ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += 1/a[i]
    print(1/sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += 1 / A[i]
    print(1 / sum)

=======
Suggestion 4

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    sum = 0
    for a in a_list:
        sum += 1/a
    print(1/sum)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    tmp = 0
    for i in range(n):
        tmp += 1/a[i]
    print(1/tmp)

=======
Suggestion 6

def main():
    N = int(input())
    A = input().split()
    A = [int(s) for s in A]
    sum = 0
    for i in A:
        sum += 1/i
    print(1/sum)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1.0/sum([1.0/a for a in A]))

=======
Suggestion 8

def calc_inverse_sum(n, list):
    sum = 0
    for i in range(n):
        sum += 1 / list[i]
    return 1 / sum

n = int(input())
list = list(map(int, input().split()))
print(calc_inverse_sum(n, list))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(1 / sum([1 / a for a in A]))

main()  # 出力結果：AC
