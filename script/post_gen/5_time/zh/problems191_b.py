Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    result = []
    for i in range(n):
        if a[i] != x:
            result.append(a[i])
    print(*result)

=======
Suggestion 2

def remove_x_from_a(a, x):
    new_a = [i for i in a if i != x]
    return new_a

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=" ")

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] != x:
            ans.append(a[i])
    print(*ans)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != x:
            print(a[i], end=" ")
    print()

=======
Suggestion 6

def problem191_b():
    #输入
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    #处理
    result = []
    for i in range(n):
        if a[i] != x:
            result.append(a[i])

    #输出
    for i in range(len(result)):
        if i != 0:
            print(" ", end="")
        print(result[i], end="")
    print()

=======
Suggestion 7

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A = [i for i in A if i != X]
    print(*A)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = [int(x) for x in input().split()]
    for i in range(n):
        if a[i] != x:
            print(a[i], end=' ')
