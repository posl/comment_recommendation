Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    for i in range(4):
        if s[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    for i in S:
        if i == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 3

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
Suggestion 4

def main():
    S = input()
    result = 0
    for i in S:
        if i == '+':
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 5

def solve(S):
    ans = 0
    for s in S:
        if s == '+':
            ans += 1
        else:
            ans -= 1
    return ans

S = input()
print(solve(S))

=======
Suggestion 6

def main():
    S = input()
    print(S.count('+') - S.count('-'))

=======
Suggestion 7

def solve():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 8

def main():
    """Main function."""
    s = input()
    print(s.count("+") - s.count("-"))
