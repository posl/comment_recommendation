Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    C1, C2, C3 = input().split()
    if C1 == C2 and C2 == C3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 2

def main():
    C1, C2, C3 = input().split()
    if C1 == C2 == C3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 3

def main():
    c1, c2, c3 = input().split()
    if c1 == c2 == c3:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 4

def main():
    C1, C2, C3 = input().split()
    if C1 == C2 == C3:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 6

def main():
    C = input().split()
    if C[0] == C[1] == C[2]:
        print('Won')
    else:
        print('Lost')

main()

=======
Suggestion 7

def main():
    list = input().split()
    if list[0] == list[1] == list[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 8

def main():
    c = input()
    print("Won" if len(set(c)) == 1 else "Lost")
