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
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if H <= sum(A) else "No")

=======
Suggestion 3

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if H > A[-1]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[-1] >= H:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    # 入力
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 処理
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print('Yes' if h > sum(a) else 'No')

=======
Suggestion 8

def main():
    h,n,*a=map(int,open(0).read().split())
    print('Yes' if h<=sum(a) else 'No')
