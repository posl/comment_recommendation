Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] == S[1] or S[1] == S[2]:
        print(2)
    else:
        print(0)

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(1)
    elif s[0] == s[1] or s[1] == s[2]:
        print(2)
    else:
        print(0)

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(0)
    elif s[0] == s[1] or s[1] == s[2]:
        print(1)
    else:
        print(2)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    max_count = 0
    for i in s:
        if i == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 5

def main():
    s = input()
    count = 0
    max = 0
    for i in s:
        if i == 'R':
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 6

def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(3):
        if s[i] == "R":
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 7

def main():
    s = input()
    c = 0
    max = 0
    for i in range(3):
        if s[i] == 'R':
            c += 1
        else:
            c = 0
        if max < c:
            max = c
    print(max)

=======
Suggestion 8

def main():
    S = input()
    S = S.replace('S', '0')
    S = S.replace('R', '1')
    print(S.count('0'))

=======
Suggestion 9

def main():
    weather = input()
    print(weather.count('R'))

main()

=======
Suggestion 10

def main():
    S = input()
    print(S.count("R"))
    return
