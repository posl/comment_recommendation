Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 2

def main():
    # input
    C1, C2, C3 = input().split()

    # compute

    # output
    if C1 == C2 and C2 == C3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 3

def main():
    c = input()
    if c[0] == c[1] == c[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 4

def main():
    c1, c2, c3 = input().rstrip().split()
    if c1 == c2 and c2 == c3:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 5

def main():
    c1,c2,c3 = input().split()
    if c1 == c2 == c3:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 6

def main():
    # input
    C1, C2, C3 = input().split()

    # compute
    if C1 == C2 and C2 == C3:
        result = 'Won'
    else:
        result = 'Lost'

    # output
    print(result)

=======
Suggestion 7

def main():
    # input
    C = list(input())
    # compute
    if C[0] == C[1] == C[2]:
        result = 'Won'
    else:
        result = 'Lost'
    # output
    print(result)

=======
Suggestion 8

def main():
    c1,c2,c3 = input().rstrip().split()
    if c1 == c2 == c3:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 9

def main():
    #input
    C_1, C_2, C_3 = input().split()
    #compute
    if C_1 == C_2 == C_3:
        result = "Won"
    else:
        result = "Lost"
    #output
    print(result)

=======
Suggestion 10

def main():
    #data = input().split()
    #c1 = data[0]
    #c2 = data[1]
    #c3 = data[2]
    #if c1 == c2 and c2 == c3:
    #    print("Won")
    #else:
    #    print("Lost")
    print("Won" if len(set(input())) == 1 else "Lost")
