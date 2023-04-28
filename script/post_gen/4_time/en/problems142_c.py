Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(*b)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(' '.join(map(str, B)))

=======
Suggestion 4

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    return b

n = int(input())
a = list(map(int, input().split()))
print(*solve(n, a))

=======
Suggestion 5

def problem142_c():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(*B)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append([A[i], i+1])
    B.sort()
    for i in range(N):
        print(B[i][1], end=" ")
    print()

=======
Suggestion 7

def main():
    num = int(input())
    input_list = input().split(" ")
    output_list = [0] * num
    for i in range(num):
        output_list[int(input_list[i]) - 1] = i + 1
    print(*output_list)
