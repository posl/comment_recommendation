Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    number = int(input())
    counter = 0
    for i in range(1, number + 1):
        if len(str(i)) % 2 != 0:
            counter += 1
    print(counter)

=======
Suggestion 5

def count_odd_digits(num):
    count = 0
    for i in range(1, num + 1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

=======
Suggestion 6

def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

=======
Suggestion 7

def main():
    n = input()
    print(len([i for i in range(1, n+1) if len(str(i)) % 2 == 1]))

=======
Suggestion 8

def count_odd_digits(n):
    # 1桁の場合
    if n < 10:
        return 1

    # 2桁以上の場合
    count = 9
    for i in range(10, n + 1):
        if len(str(i)) % 2 == 1:
            count += 1

    return count
