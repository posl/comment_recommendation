Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = ""
    while N > 0:
        N -= 1
        ans = chr(ord('a') + N % 26) + ans
        N //= 26
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = ''
    while n > 0:
        n -= 1
        ans += chr(ord('a') + n % 26)
        n //= 26
    print(ans[::-1])

=======
Suggestion 3

def name(n):
    if n <= 26:
        return chr(96 + n)
    else:
        return name((n - 1) // 26) + chr(96 + (n - 1) % 26 + 1)

print(name(int(input())))

Sample Input 1

2

Sample Output 1

b

Sample Input 2

27

Sample Output 2

aa

Sample Input 3

123456789

Sample Output 3

jjddja

I don't understand why the second sample input is aa instead of aaa

It's because of the way the problem is defined. The dogs numbered 1, 2, ... are respectively given the following names: a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., abz, ..., zzz, aaaa, ... . So the 27th dog is named aa .

I don't understand why the second sample input is aa instead of aaa

It's because of the way the problem is defined. The dogs numbered 1, 2, ... are respectively given the following names: a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., abz, ..., zzz, aaaa, ... . So the 27th dog is named aa .

It's because of the way the problem is defined.

The dogs numbered 1, 2, ... are respectively given the following names: a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., abz, ..., zzz, aaaaa, ... . So the 27th dog is named aa .

I don't understand why the second sample input is aa instead of aaa

It's because of the way the problem is defined. The dogs numbered 1, 2, ... are respectively given the following names: a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., ab

=======
Suggestion 4

def main():
    n = int(input())
    s = ""
    while n > 0:
        n -= 1
        s = chr(n%26 + ord("a")) + s
        n //= 26
    print(s)

=======
Suggestion 5

def get_name(n):
    if n <= 26:
        return chr(ord('a') + n - 1)
    else:
        return get_name((n-1) // 26) + get_name((n-1) % 26 + 1)

=======
Suggestion 6

def get_name(n):
    name = ''
    while n > 0:
        n -= 1
        name += chr(ord('a') + n % 26)
        n //= 26
    return name[::-1]

=======
Suggestion 7

def main():
    n = int(input())
    s = ""
    while n > 0:
        n -= 1
        a = n % 26
        s = chr(a+97) + s
        n = n // 26
    print(s)

=======
Suggestion 8

def getDogName(n):
    base = 26
    name = ''
    while n > 0:
        n -= 1
        name = chr(ord('a') + n % base) + name
        n //= base
    return name

=======
Suggestion 9

def dogs(n):
    # 26^0 = 1
    # 26^1 = 26
    # 26^2 = 676
    # 26^3 = 17576
    # ...
    # 26^k = 26^k-1 * 26
    # 26^k = 26^(k-1) * 26
    # 26^k = 26^(k-1) * 26^1
    # 26^k = 26^(k-1) * 26^(0+1)
    # 26^k = 26^(k-1) * 26^0 * 26^1
    # 26^k = 26^(k-1) * 26^1
    # 26^k = 26^(k-1) * 26

=======
Suggestion 10

def intToName(n):
    if n == 0:
        return ""
    else:
        return intToName((n-1)/26) + chr((n-1)%26 + 97)

n = input()
print intToName(n)
