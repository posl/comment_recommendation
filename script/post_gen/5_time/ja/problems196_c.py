Synthesizing 10/10 solutions

=======
Suggestion 1

def is_even_length(x):
    return len(str(x)) % 2 == 0

=======
Suggestion 2

def check(x):
    s = str(x)
    if len(s) % 2 == 1:
        return False
    
    for i in range(len(s)//2):
        if s[i] != s[i+len(s)//2]:
            return False
    return True

n = int(input())
ans = 0
for i in range(1, n+1):
    if check(i):
        ans += 1
print(ans)

=======
Suggestion 3

def is_even_digit(x):
    return len(str(x)) % 2 == 0

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                count += 1
    print(count)

=======
Suggestion 5

def get_half(n):
    n = str(n)
    return n[:len(n) // 2]

=======
Suggestion 6

def main():
    n = int(input())
    print(sum([1 for i in range(1, n+1) if len(str(i)) % 2 == 0 and str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]]))

=======
Suggestion 7

def main():
    N = int(input())
    if N < 11:
        print(0)
        return
    if N < 100:
        print(1)
        return
    if N < 1000:
        print(2)
        return
    if N < 10000:
        print(3)
        return
    if N < 100000:
        print(4)
        return
    if N < 1000000:
        print(5)
        return
    if N < 10000000:
        print(6)
        return
    if N < 100000000:
        print(7)
        return
    if N < 1000000000:
        print(8)
        return
    if N < 10000000000:
        print(9)
        return
    if N < 100000000000:
        print(10)
        return
    if N < 1000000000000:
        print(11)
        return
    if N < 10000000000000:
        print(12)
        return
    if N < 100000000000000:
        print(13)
        return
    if N < 1000000000000000:
        print(14)
        return
    if N < 10000000000000000:
        print(15)
        return
    if N < 100000000000000000:
        print(16)
        return
    if N < 1000000000000000000:
        print(17)
        return
    if N < 10000000000000000000:
        print(18)
        return
    if N < 100000000000000000000:
        print(19)
        return
    if N < 1000000000000000000000:
        print(20)
        return
    if N < 10000000000000000000000:
        print(21)
        return
    if N < 100000000000000000000000:
        print(22)
        return
    if N < 1000000000000000000000000:
        print(23)
        return
    if N < 10000000000000000000000000:
        print(24)
        return
    if N < 100000000000000000000000000:
        print

=======
Suggestion 8

def is_even_digits(n):
    if len(str(n)) % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 9

def is_double(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    return s[:len(s)//2] == s[len(s)//2:]

=======
Suggestion 10

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                ans += 1
    print(ans)
