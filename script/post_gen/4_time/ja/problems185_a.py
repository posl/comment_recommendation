Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a1, a2, a3, a4 = map(int, input().split())
    print(min(a1, a2, a3, a4))

=======
Suggestion 2

def main():
    # input
    A_1, A_2, A_3, A_4 = map(int, input().split())

    # compute

    # output
    if A_1 + A_2 + A_3 + A_4 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    ans = 0
    for i in range(len(A)):
        ans += A[i] // 100
        ans += A[i] % 100
    print(ans // 100)

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    print(min(a))

=======
Suggestion 5

def main():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    print(min(a))

=======
Suggestion 6

def main():
    A = list(map(int, input().split()))
    print(min(A))

=======
Suggestion 7

def main():
    A = [int(i) for i in input().split()]
    print(min(A))
