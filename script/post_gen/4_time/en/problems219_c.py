Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(26):
        d[x[i]] = chr(ord('a') + i)
    for i in range(n):
        s[i] = ''.join([d[c] for c in s[i]])
    s.sort()
    for i in range(n):
        print(''.join([x[ord(c) - ord('a')] for c in s[i]]))

=======
Suggestion 2

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        for j in range(26):
            s[i] = s[i].replace(x[j], chr(97+j))
    for i in range(n):
        for j in range(26):
            s[i] = s[i].replace(chr(97+j), x[j])
    s.sort()
    for i in range(n):
        for j in range(26):
            s[i] = s[i].replace(x[j], chr(97+j))
    for i in range(n):
        print(s[i])

=======
Suggestion 3

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = sorted(s, key=lambda s: [x.index(c) for c in s])
    print(*s, sep='\n')

=======
Suggestion 4

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [x[i] for i in range(len(x))])
    print("\n".join(s))

=======
Suggestion 5

def main():
  x = input()
  n = int(input())
  s = []
  for i in range(n):
    s.append(input())
  s.sort(key=lambda s: [x.index(c) for c in s])
  for i in s:
    print(i)

=======
Suggestion 6

def main():
    x = input()
    n = int(input())
    s = [input() for i in range(n)]
    d = dict(zip(x, range(26)))
    s.sort(key=lambda x: [d[c] for c in x])
    print(*s, sep="\n")

=======
Suggestion 7

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x:[x.translate(str.maketrans(x,'abcdefghijklmnopqrstuvwxyz'))])
    for i in range(n):
        print(s[i])

=======
Suggestion 8

def solve():
    x = input()
    n = int(input())

    s = []
    for i in range(n):
        s.append(input())

    for i in range(n):
        s[i] = s[i].translate(str.maketrans(x, 'abcdefghijklmnopqrstuvwxyz'))

    s.sort()
    for i in range(n):
        s[i] = s[i].translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', x))
        print(s[i])

=======
Suggestion 9

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: ''.join([chr(96 - ord(c)) for c in x]))
    for i in range(n):
        print(s[i])

=======
Suggestion 10

def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    y = sorted(s, key=lambda x: [x[i] for i in range(len(x))])

    for i in range(n):
        print(y[i])
