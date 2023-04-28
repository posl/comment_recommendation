Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    counter = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            counter += 1
    print(counter)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)
main()

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    # Take input here
    S = input()
    T = input()

    # Computing result
    result = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            result += 1

    # Print result
    print(result)

=======
Suggestion 7

def main():
    S = input()
    T = input()
    print(sum([1 for s, t in zip(S, T) if s != t]))
