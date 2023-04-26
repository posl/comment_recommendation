Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

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
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = input()
    if int(n) % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    n = int(input())
    if n%9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = input()
    #print(n)
    sum = 0
    for i in n:
        sum += int(i)
    #print(sum)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n = int(input())
    if n%9==0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def nine_multiple(n):
    n_list = list(map(int, str(n)))
    if sum(n_list) % 9 == 0:
        return 'Yes'
    else:
        return 'No'

n = int(input())
print(nine_multiple(n))
