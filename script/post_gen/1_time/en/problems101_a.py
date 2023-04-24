Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    num = 0
    for i in range(4):
        if S[i] == "+":
            num += 1
        else:
            num -= 1
    print(num)

=======
Suggestion 2

def main():
    S = input()
    #print(S)
    count = 0
    for i in range(4):
        if S[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 3

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 4

def main():
    S = input()
    print(S.count('+') - S.count('-'))

=======
Suggestion 5

def main():
    S = input()
    print(S.count("+") - S.count("-"))

=======
Suggestion 6

def main():
    # get input
    s = input()
    # count + and - and print sum
    print(s.count('+') - s.count('-'))
