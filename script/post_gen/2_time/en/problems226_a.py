Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = input()
    if int(X[2]) >= 5:
        print(int(X[0]) + 1)
    else:
        print(int(X[0]))

=======
Suggestion 2

def round_to_nearest_int(x):
    if x % 1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)

x = float(input())
print(round_to_nearest_int(x))

=======
Suggestion 3

def round(x):
    if x % 1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)

=======
Suggestion 4

def main():
    x = float(input())
    print(int(x+0.5))

=======
Suggestion 5

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 6

def main():
    x = float(input())
    print(int(round(x)))

=======
Suggestion 7

def main():
    X = float(input())
    print(int(round(X)))

=======
Suggestion 8

def main():
    x = input()
    print(round(float(x)))

=======
Suggestion 9

def main():
    #input
    X = input().strip()
    X = float(X)
    #print(X)
    #X = float(X)
    #pri
