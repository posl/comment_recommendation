Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = 'o' * 100000 + 'x' * 100000
    if s in t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    S = input()
    T = 'ox'*10**5
    if S in T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = 'o' * 100000
    if s in t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    if 'o' in s and 'x' in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    if s.count('o') + (15 - len(s)) >= 8:
        print('YES')
    else:
        print('NO')

=======
Suggestion 6

def main():
    s = input()
    if s.find('o') >= 0 and s.find('x') >= 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input()
    T = "o" + S + "x"
    print("Yes" if T in "oxx" * 100000 else "No")

=======
Suggestion 8

def main():
    s = input()
    t = 'o' + s + 'o'
    print('Yes' if t.find('oo') != -1 else 'No')
main()

=======
Suggestion 9

def main():
    s = input()
    print('Yes' if 'o' in s else 'No')

=======
Suggestion 10

def main():
    s = input()
    print('Yes' if s in 'ox' * 10**5 else 'No')
