Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    print(A.index(B[1]) + 1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    min = a[0]
    for i in range(1,n):
        if a[i] < min:
            ans += 1
            min = a[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    min1 = min(A)
    min2 = min(filter(lambda x: x != min1, A))
    for i in range(N):
        if A[i] == min2:
            print(i + 1)
            break

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])

=======
Suggestion 5

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

=======
Suggestion 6

def main():
    n = int(input())
    scores = [int(i) for i in input().split()]
    min_value = min(scores)
    scores = [i for i in scores if i != min_value]
    print(scores.index(min(scores))+1)

=======
Suggestion 7

def main():
    # 读入输入
    n = int(input())
    a = list(map(int, input().split()))

    # 排序
    a.sort()

    # 打印答案
    print(a[1])

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    print(A.index(A_sorted[1])+1)

solve()
