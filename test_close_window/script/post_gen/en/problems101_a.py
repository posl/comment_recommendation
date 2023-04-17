Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    s = input()
    ans = 0
    for i in s:
        if i == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======

def main():
    S = input()
    ans = 0
    for i in S:
        if i == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======

def main():
    S = input()
    ans = 0
    for i in S:
        if i == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)

=======

def main():
    S = input()
    count = 0
    for i in S:
        if i == "+":
            count += 1
        else:
            count -= 1
    print(count)

=======

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======

def main():
    S = input()
    print(S.count('+') - S.count('-'))

=======

def main():
    S = input()
    print(S.count("+") - S.count("-"))

=======

def count_plus_minus(s):
    return s.count('+') - s.count('-')
