Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if H <= sum(A) else "No")

=======
Suggestion 4

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))

    if H <= sum(A):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print('Yes' if H <= sum(A) else 'No')

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 8

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    print("Yes" if h <= sum(a) else "No")
