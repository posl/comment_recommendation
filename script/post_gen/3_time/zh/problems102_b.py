Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(a[i]-a[j]) > max:
                max = abs(a[i]-a[j])
    print(max)

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(max(a)-min(a))

main()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1]-a[0])

=======
Suggestion 5

def max_absolute_difference(n, a):
    a.sort()
    return a[-1] - a[0]

=======
Suggestion 6

def get_max_abs_diff():
    n = int(input())
    a = list(map(int, input().split()))
    min_num = a[0]
    max_num = a[0]
    for i in a:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return max_num - min_num

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A)-min(A))
