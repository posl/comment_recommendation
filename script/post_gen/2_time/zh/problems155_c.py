Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 判断是否存在不符合条件的数字
    for i in range(n):
        if a[i] % 2 == 0 and a[i] % 3 != 0 and a[i] % 5 != 0:
            print("DENIED")
            return
    print("APPROVED")
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] % 2 == 0 and A[i] % 3 != 0 and A[i] % 5 != 0:
            print('DENIED')
            return
    print('APPROVED')
    return

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    flag = True
    for i in a:
        if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):
            flag = False
            break
    if flag:
        print("APPROVED")
    else:
        print("DENIED")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
            print("DENIED")
            exit()
    print("APPROVED")
main()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 == 0 or a[i] % 5 == 0:
                pass
            else:
                print("DENIED")
                exit(0)
    print("APPROVED")

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0 and (a[i] % 3 != 0 and a[i] % 5 != 0):
            print("DENIED")
            exit()
    print("APPROVED")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print('DENIED')
                exit()
    print('APPROVED')

=======
Suggestion 8

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
solve()

=======
Suggestion 10

def check_evenly_divisible(number):
    if number % 3 == 0 or number % 5 == 0:
        return True
    else:
        return False
