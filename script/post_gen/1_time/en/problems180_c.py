Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = set()
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.add(i)
            ans.add(N//i)
    for i in sorted(ans):
        print(i)

=======
Suggestion 2

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 3

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans.append(i)
            if i != N//i:
                ans.append(N//i)
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 4

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            if i != N//i:
                ans.append(N//i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 5

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i != N // i:
                print(N // i)
        i += 1

main()

=======
Suggestion 6

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            ans.append(i)
            if n//i != i:
                ans.append(n//i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            print(i)
            if i != N//i:
                print(N//i)

=======
Suggestion 8

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            if i*i != N:
                ans.append(N//i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 9

def puffs():
    N = int(input())
    ans = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans.append(i)
            ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 10

def  main():
     N  =  int (input())
