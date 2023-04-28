Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    str = input()
    red = 0
    blue = 0
    for i in str:
        if i == '0':
            red += 1
        else:
            blue += 1
    print(min(red, blue) * 2)

=======
Suggestion 2

def main():
    s = input()
    print(min(s.count('0'), s.count('1')) * 2)

=======
Suggestion 3

def main():
    S = input()

    count = 0
    for i in range(len(S)):
        if i == 0:
            continue
        if S[i-1] != S[i]:
            count += 1

    print(count)

=======
Suggestion 4

def main():
    # input
    S = input()

    # compute

    # output
    print(min(S.count('0'), S.count('1')) * 2)

=======
Suggestion 5

def main():
    S = input()
    R = S.count("0")
    B = S.count("1")
    print(min(R, B) * 2)

=======
Suggestion 6

def solve():
    S = input()
    print(min(S.count('0'), S.count('1')) * 2)
