Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print("bust")
    else:
        print("win")

main()

=======
Suggestion 2

def main():
    a1, a2, a3 = map(int, input().split())
    if a1 + a2 + a3 >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 3

def main():
    A1, A2, A3 = map(int, input().split())
    if A1 + A2 + A3 >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 4

def main():
    A1, A2, A3 = map(int, input().split())
    if A1+A2+A3 >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 5

def main():
    A = list(map(int, input().split()))
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

main()

=======
Suggestion 6

def main():
    A = list(map(int, input().split()))
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 7

def main():
    A = [int(a) for a in input().split()]
    if sum(A) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 8

def main():
    a = input().split()
    a = [int(x) for x in a]
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 9

def main():
    a, b, c = map(int, input().split())
    print("bust" if a+b+c>=22 else "win")

=======
Suggestion 10

def main():
    #input
    A = list(map(int, input().split()))
    #output
    print('bust' if sum(A) >= 22 else 'win')
