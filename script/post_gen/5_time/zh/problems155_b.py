Synthesizing 10/10 solutions

=======
Suggestion 1

def is_even(x):
    return x % 2 == 0

=======
Suggestion 2

def solve(n, a):
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                return "DENIED"
    return "APPROVED"

=======
Suggestion 3

def isOk(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    else:
        return False

N = int(input())
A = list(map(int, input().split()))

flag = True
for i in range(N):
    if not isOk(A[i]):
        flag = False

=======
Suggestion 4

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 5

def check(n):
    if n % 2 == 0 and (n % 3 == 0 or n % 5 == 0):
        return True
    else:
        return False

=======
Suggestion 6

def main():
    n=int(input())
    a=list(map(int,input().split()))
    for i in a:
        if i%2==0:
            if i%3!=0 and i%5!=0:
                print("DENIED")
                exit()
    print("APPROVED")

=======
Suggestion 7

def is_divisible_by_3_or_5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if a%2==0 and (a%3!=0 and a%5!=0):
            print("DENIED")
            return
    print("APPROVED")
    return

=======
Suggestion 9

def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))

    # 检查条件
    for a in A:
        if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
            print("DENIED")
            return

    # 输出结果
    print("APPROVED")

main()

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print('DENIED')
                return
    print('APPROVED')
main()
