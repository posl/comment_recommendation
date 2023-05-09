Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    print('Yes' if s == t else 'No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    print("Yes" if S == T else "No")

=======
Suggestion 5

def main():
    # input
    S = input()
    T = input()

    # compute

    # output
    print('Yes' if S == T else 'No')

=======
Suggestion 6

def main():
    #s = input()
    #s = s.split()
    #t = input()
    #t = t.split()
    s = ['R', 'G', 'B']
    t = ['R', 'G', 'B']
    for i in range(3):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    print("Yes") if s == t else print("No")

=======
Suggestion 8

def main():
    # Take input Here and Call solution function
    colors = list(map(str, input().strip().split()))
    goals = list(map(str, input().strip().split()))
    if colors[0] == goals[0] and colors[1] == goals[1] and colors[2] == goals[2]:
        print("Yes")
    else:
        print("No")
    pass
