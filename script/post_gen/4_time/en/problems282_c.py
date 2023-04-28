Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        if s[i] == '"':
            count += 1
        if s[i] == ',' and count % 2 == 0:
            s = s[:i] + '.' + s[i+1:]
    print(s)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    for i in range(1, n-1):
        if s[i] == ',' and s[i-1] != '"' and s[i+1] != '"':
            s = s[:i] + '.' + s[i+1:]
    print(s)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(n):
        if s[i] == ',':
            if i % 2 == 0:
                s[i] = '.'
    print(''.join(s))

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    for i in range(0, n):
        if s[i] == ',':
            if (i + 1) % 2 == 0:
                print('.', end='')
            else:
                print(s[i], end='')
        else:
            print(s[i], end='')
    print()

=======
Suggestion 5

def solve():
    n = int(input())
    s = input()
    t = ""
    c = 0
    for i in range(n):
        if s[i] == '"':
            c += 1
            if c % 2 == 1:
                t += '"'
            else:
                t += '.'
        else:
            t += s[i]
    print(t)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(n):
        if i % 2 == 0:
            if s[i] == ',':
                s[i] = '.'
        else:
            if s[i] == '"':
                s[i] = ','
    print(''.join(s))

=======
Suggestion 7

def main():
    N = int(input())
    S = input()

    if N % 2 == 1:
        print("error")
        return

    if S.count('"') % 2 == 1:
        print("error")
        return

    result = ""
    in_enclosed = False
    for c in S:
        if c == '"':
            in_enclosed = not in_enclosed
        elif c == ',' and not in_enclosed:
            result += '.'
        else:
            result += c

    print(result)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    s = list(s)
    for i in range(n):
        if s[i] == ",":
            if (s[:i].count('"') + s[i+1:].count('"')) % 2 == 0:
                s[i] = "."
    print("".join(s))

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        print(S.replace(",", "."))
    else:
        print("error")

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    s = s.replace(",",".")
    s = s.replace("\"","")
    s = s.replace(".","\",")
    print("\""+s)
