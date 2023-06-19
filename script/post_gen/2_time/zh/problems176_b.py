Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def is_multiple_of_9(n):
    if n == 0:
        return True
    if n % 9 == 0:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    N = input()
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = input()
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    if total % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = input()
    n = list(n)
    n = list(map(int, n))
    sum = 0
    for i in n:
        sum += i
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # 读入数据
    N = input()
    # 处理数据
    sum = 0
    for i in N:
        sum += int(i)
    # 输出结果
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")
main()
