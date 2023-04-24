Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    total = 0
    for i in range(1, n+1):
        total += i
        if total >= n:
            print(i)
            break

=======
Suggestion 2

def main():
    N = int(input())
    x = 0
    for i in range(1, N+1):
        x += i
        if x >= N:
            print(i)
            break

=======
Suggestion 3

def main():
    n = int(input())
    total = 0
    for i in range(1, 100000):
        total += i
        if total >= n:
            print(i)
            break

=======
Suggestion 4

def resolve():
    N = int(input())
    i = 0
    while True:
        i += 1
        N -= i
        if N <= 0:
            print(i)
            break

=======
Suggestion 5

def main():
    n = int(input())
    sum = 0
    count = 0
    while(sum < n):
        count += 1
        sum += count
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    for i in range(1, N+1):
        if i*(i+1)//2 >= N:
            print(i)
            break

=======
Suggestion 7

def main():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            print(i)
            exit()
        else:
            pass

=======
Suggestion 8

def main():
    N = int(input())
    for i in range(1, N+1):
        if N <= i*(i+1)/2:
            print(i)
            exit()

=======
Suggestion 9

def main():
    n = int(input())
    i = 1
    while i*(i+1)//2 < n:
        i += 1
    print(i)
    return
