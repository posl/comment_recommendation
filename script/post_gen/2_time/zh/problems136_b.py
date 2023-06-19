Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        elif i < 100:
            count += 1
        elif i < 1000:
            count += 2
        elif i < 10000:
            count += 2
        elif i < 100000:
            count += 3
    print(count)

=======
Suggestion 2

def main():
    # N = int(input())
    # print(len([i for i in range(1, N+1) if i % 2 == 1]))
    print(len([i for i in range(1, int(input())+1) if i % 2 == 1]))

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        elif i < 100:
            if i % 2 == 1:
                count += 1
        elif i < 1000:
            if i % 2 == 1:
                count += 2
        elif i < 10000:
            if i % 2 == 1:
                count += 2
        elif i < 100000:
            if i % 2 == 1:
                count += 3
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 5

def solution(N):
    count = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            count += 1
    return count

N = int(input())
print(solution(N))

=======
Suggestion 6

def count_odd(n):
    if n < 10:
        return n
    else:
        count = 9
        for i in range(10, n + 1):
            if i % 10 % 2 == 1:
                count += 1
        return count

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i < 10:
            count += 1
        elif i < 100:
            count += 1
        elif i < 1000:
            count += 1
        elif i < 10000:
            count += 1
        elif i < 100000:
            count += 1
    print(count)
main()

=======
Suggestion 8

def solve(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 1:
            count += 1
    return count

=======
Suggestion 9

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        elif i < 100:
            count += 1
        elif i < 1000:
            count += 1
        elif i < 10000:
            count += 1
        elif i < 100000:
            count += 1
        elif i < 1000000:
            count += 1
        elif i < 10000000:
            count += 1
        elif i < 100000000:
            count += 1
        elif i < 1000000000:
            count += 1
        elif i < 10000000000:
            count += 1
        elif i < 100000000000:
            count += 1
        elif i < 1000000000000:
            count += 1
        elif i < 10000000000000:
            count += 1
        elif i < 100000000000000:
            count += 1
        elif i < 1000000000000000:
            count += 1
        elif i < 10000000000000000:
            count += 1
        elif i < 100000000000000000:
            count += 1
        elif i < 1000000000000000000:
            count += 1
        elif i < 10000000000000000000:
            count += 1
        elif i < 100000000000000000000:
            count += 1
        elif i < 1000000000000000000000:
            count += 1
        elif i < 10000000000000000000000:
            count += 1
        elif i < 100000000000000000000000:
            count += 1
        elif i < 1000000000000000000000000:
            count += 1
        elif i < 10000000000000000000000000:
            count += 1
        elif i < 100000000000000000000000000:
            count += 1
        elif i < 1000000000000000000000000000:
            count += 1
        elif i < 100

=======
Suggestion 10

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if i < 10:
            cnt += 1
        elif i < 100:
            cnt += 1
        elif i < 1000:
            cnt += 1
        elif i < 10000:
            cnt += 1
        elif i < 100000:
            cnt += 1
    print(cnt)
main()
