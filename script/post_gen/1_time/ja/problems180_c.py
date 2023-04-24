Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 2

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 3

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans.append(i)
            if N//i != i:
                ans.append(N//i)
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            if N//i != i:
                ans.append(N//i)
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            print(i)
            if N//i != i:
                print(N//i)

=======
Suggestion 6

def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.append(i)
            if i * i != N:
                ans.append(N//i)
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    N = int(input())
    divisors = []
    i = 1
    while i*i <= N:
        if N%i == 0:
            divisors.append(i)
            if i*i != N:
                divisors.append(N//i)
        i += 1
    divisors.sort()
    for d in divisors:
        print(d)

=======
Suggestion 8

def main():
    n = int(input())
    # 約数を求める
    div = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            div.append(i)
            if i**2 != n:
                div.append(n//i)
    div.sort()
    for i in div:
        print(i)
