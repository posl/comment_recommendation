Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(3):
        if S[i] == T[i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    result = 0
    for i in range(3):
        if s[i] == t[i]:
            result += 1
    print(result)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    counter = 0
    for i in range(3):
        if s[i] == t[i]:
            counter += 1
    print(counter)

=======
Suggestion 6

def main():
    # input
    S = input()
    T = input()
    # compute
    count = 0
    for i in range(3):
        if S[i] == T[i]:
            count += 1
    # output
    print(count)

=======
Suggestion 7

def main():
    S = input()
    T = input()
    print(sum([1 for i in range(3) if S[i] == T[i]]))
