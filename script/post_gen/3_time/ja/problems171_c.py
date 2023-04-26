Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = ''
    while n > 0:
        n -= 1
        ans = chr(ord('a') + n % 26) + ans
        n //= 26
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = ""
    while n > 0:
        n -= 1
        ans += chr(ord('a') + n % 26)
        n //= 26
    print(ans[::-1])

=======
Suggestion 3

def main():
    N = int(input())
    ans = ''
    while N > 0:
        N -= 1
        ans = chr(ord('a') + N % 26) + ans
        N //= 26
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = []
    while n > 0:
        n -= 1
        ans.append(chr(ord('a') + (n % 26)))
        n //= 26
    print(''.join(ans[::-1]))

=======
Suggestion 5

def main():
    N = int(input())
    name = ''
    while N > 0:
        N -= 1
        name = chr(ord('a') + N % 26) + name
        N //= 26
    print(name)

=======
Suggestion 6

def convert(num):
    if num == 0:
        return ""
    else:
        return convert((num - 1) // 26) + chr((num - 1) % 26 + ord("a"))

n = int(input())
print(convert(n))

=======
Suggestion 7

def get_str(n):
    if n <= 26:
        return chr(ord('a') + n - 1)
    else:
        return get_str((n - 1) // 26) + chr(ord('a') + (n - 1) % 26)

=======
Suggestion 8

def get_char(n):
    if n <= 26:
        return chr(96+n)
    else:
        return get_char((n-1)//26) + chr(96+(n-1)%26+1)

n = int(input())
print(get_char(n))

=======
Suggestion 9

def calc(n):
    if n == 0:
        return ""
    elif n <= 26:
        return chr(96+n)
    else:
        if n % 26 == 0:
            return calc(n//26-1) + chr(122)
        else:
            return calc(n//26) + chr(96+n%26)

n = int(input())
print(calc(n))
