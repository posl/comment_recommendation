Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    if N < 10:
        print(N)
    elif N < 100:
        print(9)
    elif N < 1000:
        print(9 + N - 99)
    elif N < 10000:
        print(9 + 900)
    elif N < 100000:
        print(9 + 900 + N - 9999)
    else:
        print(9 + 900 + 90000)

=======
Suggestion 4

def main():
    n = int(input())
    cnt = 0
    for i in range(1,n+1):
        if len(str(i))%2 == 1:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    odd = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            odd += 1
    print(odd)

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if len(str(i))%2 != 0:
            count = count + 1
    print(count)

=======
Suggestion 7

def main():
    N = input()
    N = int(N)
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    if n < 10:
        print(n)
        return
    result = 9
    if n < 100:
        print(result)
        return
    if n < 1000:
        result += n - 99
        print(result)
        return
    if n < 10000:
        result += 900
        result += n - 999
        print(result)
        return
    if n < 100000:
        result += 900
        result += 90000
        result += n - 9999
        print(result)
        return
    print(90909)
    return

=======
Suggestion 9

def find_odd_digits(N):
    odd_digits = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 != 0:
            odd_digits += 1
    return odd_digits

N = int(input())
print(find_odd_digits(N))
