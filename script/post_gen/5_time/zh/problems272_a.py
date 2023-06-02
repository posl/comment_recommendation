Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))

=======
Suggestion 3

def getSum(n, a_list):
    sum = 0
    for i in range(0, n):
        sum += a_list[i]
    return sum

=======
Suggestion 4

def calc_sum(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

num_list = []
N = int(input())
num_list = list(map(int, input().split()))
print(calc_sum(num_list))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A))

=======
Suggestion 6

def main():
    n = int(input())
    a = input().split()
    sum = 0
    for i in range(n):
        sum += int(a[i])
    print(sum)
