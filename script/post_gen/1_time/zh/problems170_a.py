Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = input()
    x = x.split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 2

def main():
    x = list(map(int, input().split()))
    print(x.index(0) + 1)

=======
Suggestion 3

def main():
    x = input().split()
    for i in range(5):
        if x[i] == "0":
            print(i+1)
            break

=======
Suggestion 4

def main():
    x = [int(i) for i in input().split()]
    print(x.index(0)+1)

=======
Suggestion 5

def main():
    x = input().split(" ")
    for i in range(0, len(x)):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 6

def main():
    x = input().split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)

=======
Suggestion 7

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 8

def problems170_a():
    x = input().split()
    for i in range(len(x)):
        if x[i] == '0':
            print(i+1)

=======
Suggestion 9

def main():
    x = input().split(' ')
    for i in range(5):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 10

def main():
    a = input().split()
    for i in range(5):
        if a[i] == '0':
            print(i+1)
            break
