Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
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
Suggestion 2

def main():
    n = int(input())
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            ans.append(n // i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 3

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans.append(i)
            if N // i != i:
                ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 4

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            ans.append(N//i)
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 5

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans.append(i)
            if i != N//i:
                ans.append(N//i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 6

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
Suggestion 7

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
Suggestion 8

def main():
    N = int(input())
    result = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            result.append(i)
            if i != N // i:
                result.append(N // i)
    result.sort()
    for i in result:
        print(i)
