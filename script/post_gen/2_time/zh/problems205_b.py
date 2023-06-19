Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    if sorted(a) == list(range(1, n+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def is_permutation(A):
    if len(A) == 1:
        return True
    else:
        B = []
        for i in range(1, len(A)+1):
            B.append(i)
        A.sort()
        if A == B:
            return True
        else:
            return False

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n+1)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == len(a):
        a.sort()
        for i in range(n):
            if a[i] != i+1:
                print('No')
                exit()
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    # 解决问题
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    flag = True
    for i in range(N):
        if i+1 != A[i]:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n+1)):
        print('Yes')
    else:
        print('No')
