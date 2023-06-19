Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

=======
Suggestion 2

def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    for a in a_list:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print('DENIED')
                return
    print('APPROVED')

=======
Suggestion 3

def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))
    # compute
    for i in a:
        if i%2 == 0:
            if i%3 != 0 and i%5 != 0:
                print("DENIED")
                exit()
    # output
    print("APPROVED")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                continue
            else:
                print('DENIED')
                return
    print('APPROVED')
    return

=======
Suggestion 5

def judge(n, a):
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                return False
    return True

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 == 0 or a[i] % 5 == 0:
                continue
            else:
                print('DENIED')
                exit()
    print('APPROVED')

=======
Suggestion 7

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')
main()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0 and a[i] % 3 != 0 and a[i] % 5 != 0:
            print("DENIED")
            exit()
    print("APPROVED")
main()

=======
Suggestion 10

def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))

    # 处理
    for i in range(N):
        if A[i] % 2 == 0:
            if A[i] % 3 != 0 and A[i] % 5 != 0:
                print('DENIED')
                exit()

    # 输出结果
    print('APPROVED')
