Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 3

def get_odds(n):
    odds = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            odds += 1
    return odds

=======
Suggestion 4

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
    print(count)

=======
Suggestion 5

def count_odd_digits(n):
    count = 0
    for i in range(1, n + 1):
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
    return count

n = int(input())
print(count_odd_digits(n))

=======
Suggestion 6

def get_odd_num(n):
    count = 0
    for i in range(1, n+1):
        if i%2 != 0:
            count += 1
    return count

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
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
Suggestion 8

def count_odd(n):
    count = 0
    for i in range(1,n+1):
        if i < 10:
            count += 1
        else:
            if i % 2 != 0:
                count += 1
    return count

=======
Suggestion 9

def count_odd_digits(n):
    count = 0
    for i in range(1, n+1):
        if i < 10:
            if i % 2 == 1:
                count += 1
        else:
            if i % 2 == 1:
                count += 1
            else:
                for j in range(1, len(str(i))):
                    if int(str(i)[j]) % 2 == 1:
                        count += 1
                        break
    return count
