Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def sum_list(num_list):
    sum = 0
    for i in num_list:
        sum += i
    return sum

=======
Suggestion 2

def sum_of_integers():
    n = int(input())
    a = list(map(int, input().split()))
    return sum(a)

=======
Suggestion 3

def sum(a):
    total = 0
    for i in range(len(a)):
        total = total + a[i]
    return total

n = int(input())
a = list(map(int, input().split()))
print(sum(a))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(sum(A))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A))

main()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(a))

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(sum(a))
