Synthesizing 10/10 solutions

=======
Suggestion 1

def move_char(ch, n):
    if ch.islower():
        base = 'a'
    else:
        base = 'A'
    return chr((ord(ch) - ord(base) + n) % 26 + ord(base))

=======
Suggestion 2

def move(s, n):
    result = ''
    for c in s:
        if c.isupper():
            result += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif c.islower():
            result += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        else:
            result += c
    return result

=======
Suggestion 3

def problem146_b():
    n = int(input())
    s = input()
    s1 = ""
    for i in range(len(s)):
        if ord(s[i]) + n > 90:
            s1 += chr(ord(s[i]) + n - 26)
        else:
            s1 += chr(ord(s[i]) + n)
    print(s1)

problem146_b()

=======
Suggestion 4

def moveStr(str, n):
    if n == 0:
        return str
    result = ''
    for s in str:
        num = ord(s) + n
        if num > 90:
            num = num - 26
        result = result + chr(num)
    return result

=======
Suggestion 5

def move_str(s, n):
    s = s.upper()
    n = n % 26
    res = ''
    for i in s:
        if ord(i) + n > ord('Z'):
            res += chr(ord(i) + n - ord('Z') + ord('A') - 1)
        else:
            res += chr(ord(i) + n)
    return res

=======
Suggestion 6

def move(s, n):
    # print(s)
    # print(n)
    # print(ord('A'))
    # print(ord('Z'))
    # print(ord('a'))
    # print(ord('z'))
    # print(ord(s))
    # print(ord(s) + n)
    # print(ord(s) + n - ord('A'))
    # print(ord(s) + n - ord('A') % 26)
    # print((ord(s) + n - ord('A')) % 26)
    # print(chr(ord(s) + n - ord('A') % 26))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    # print(chr((ord(s) + n - ord('A')) % 26 + ord('A')))
    if ord(s) >= ord('A') and ord(s) <= ord('Z'):
        return chr((ord(s) + n - ord('A')) % 26 + ord('A'))
    elif ord(s) >= ord('a') and ord(s) <= ord('z'):
        return chr((ord(s) + n - ord('a')) % 26 + ord('a'))
    else:
        return s


n = int(input())
s = input()
# print(move('A', 2))
# print(move('Y', 3))
# print(move('A', 0))
# print(move('A', 26))
# print(move('A', 27))
# print(move('a', 2))
# print(move('y', 3))
# print(move('a', 0

=======
Suggestion 7

def problem146_b():
    n = int(input())
    s = input()
    ans = ''
    for c in s:
        ans += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    s2 = ""
    for i in s:
        if ord(i)+n > 90:
            s2 += chr(ord(i)+n-26)
        else:
            s2 += chr(ord(i)+n)
    print(s2)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    s = [chr(ord(i)+n) for i in s]
    s = [i if ord(i) <= ord('Z') else chr(ord(i)-26) for i in s]
    print(''.join(s))

=======
Suggestion 10

def problem146_b():
    # 获取输入
    N = int(input())
    S = input()

    # 处理
    result = ""
    for s in S:
        result += chr(ord('A') + (ord(s) - ord('A') + N) % 26)

    # 输出结果
    print(result)
