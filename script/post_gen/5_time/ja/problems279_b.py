Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if T in S:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if t in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def solve():
    S = input()
    T = input()

    if T in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def solve():
    s = input()
    t = input()
    if t in s:
        print('Yes')
    else:
        print('No')
