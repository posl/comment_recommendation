Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = 0
    for i in str(n):
        s += int(i)
    if n % s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    s = 0
    for i in str(n):
        s += int(i)
    if n % s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N = int(input())
    S = 0
    for n in str(N):
        S += int(n)
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    s = 0
    for c in str(n):
        s += int(c)
    if n % s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n = int(input())
    n_str = str(n)
    s = 0
    for i in range(len(n_str)):
        s += int(n_str[i])
    if n % s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    s = sum(map(int,str(n)))
    if n % s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = input()
    N = int(N)
    S = 0
    for i in range(len(str(N))):
        S += int(str(N)[i])
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # input
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    N = int(input())
    #print(N)
    #print(sum(map(int, str(N))))
    if N % sum(map(int, str(N))) == 0:
        print("Yes")
    else:
        print("No")
