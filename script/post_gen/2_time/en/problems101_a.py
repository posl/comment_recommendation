Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in s:
        if i == '+':
            count += 1
        else:
            count -= 1
    print(count)
main()

=======
Suggestion 2

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 3

def main():
    S = input()
    print(S.count('+') - S.count('-'))

=======
Suggestion 4

def main():
    S = input()
    print(S.count("+") - S.count("-"))

=======
Suggestion 5

def main():
    # Read input
    s = input()
    # Solve problem
    result = 0
    for i in range(4):
        if s[i] == '+':
            result += 1
        else:
            result -= 1
    # Output result
    print(result)
