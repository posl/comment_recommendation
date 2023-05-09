Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A)-min(A))

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    print(a[-1]-a[0])

=======
Suggestion 4

def diff():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    print(max_a - min_a)

diff()

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(a) for a in input().split()]
    print(max(a)-min(a))

=======
Suggestion 6

def max_abs_diff(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    return max_num - min_num
