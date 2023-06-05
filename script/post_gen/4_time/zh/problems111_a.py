Synthesizing 10/10 solutions

=======
Suggestion 1

def problems111_a():
    n=int(input())
    print(1110-n)

=======
Suggestion 2

def main():
    n = input()
    n = n.replace('1','a')
    n = n.replace('9','1')
    n = n.replace('a','9')
    print(n)

=======
Suggestion 3

def problems111_a():
    n = input()
    for i in range(len(n)):
        if n[i] == "1":
            print("9",end="")
        else:
            print("1",end="")
    print()

problems111_a()

=======
Suggestion 4

def main():
    # 读取输入
    n = int(input())
    # 用9替换1，用1替换9
    print(1110 - n)

=======
Suggestion 5

def problem111_a():
    n = int(input())
    print(1110-n)

=======
Suggestion 6

def main():
    n = input()
    print(n.replace("1","x").replace("9","1").replace("x","9"))

=======
Suggestion 7

def main():
    n = int(input())
    print(1110-n)

=======
Suggestion 8

def problem111_a():

    n = input()
    n = int(n)
    n1 = n // 100
    n2 = (n % 100) // 10
    n3 = n % 10
    n1 = 9 if n1 == 1 else 1
    n2 = 9 if n2 == 1 else 1
    n3 = 9 if n3 == 1 else 1
    print(n1 * 100 + n2 * 10 + n3)

=======
Suggestion 9

def main():
    n = input()
    print(n.replace('1','A').replace('9','1').replace('A','9'))

=======
Suggestion 10

def replace(n):
    n = str(n)
    n = n.replace('1','x')
    n = n.replace('9','1')
    n = n.replace('x','9')
    return int(n)

n = int(input())
print(replace(n))
