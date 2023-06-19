Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(0, n-1):
        if a[i] == a[i+1]:
            print("NO")
            exit()
    print("YES")

=======
Suggestion 4

def judge_pair(a):
    if len(a) == len(set(a)):
        return True
    else:
        return False

=======
Suggestion 5

def main():
    # 读取数据
    n = int(input())
    a = list(map(int, input().split()))
    # set函数去重
    if len(set(a)) == len(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")
    return

main()

=======
Suggestion 7

def main():
    N = int(input())
    A = input().split()
    if len(A) != N:
        return
    A = list(map(int, A))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print('NO')
            exit()
    print('YES')

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            break
    else:
        print("YES")

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            exit()
    print("YES")
