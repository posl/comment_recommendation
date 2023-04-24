Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda x: [X.index(c) for c in x])
    for s in S:
        print(s)

=======
Suggestion 2

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda s: [X.index(c) for c in s])
    print(*S, sep='

')

=======
Suggestion 3

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda x: [X.index(c) for c in x])
    print('

'.join(S))

=======
Suggestion 4

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S = sorted(S, key=lambda s: [X.index(c) for c in s])
    print('

'.join(S))

=======
Suggestion 5

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S = sorted(S, key=lambda x: [X.index(i) for i in x])
    for s in S:
        print(s)

=======
Suggestion 6

def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    print(*sorted(S, key=lambda x: [X.index(c) for c in x]), sep='

')

=======
Suggestion 7

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    sortS = sorted(S, key=lambda x: [X.index(c) for c in x])
    print(*sortS, sep='

')

=======
Suggestion 8

def main():
    # Input
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # Solve
    S = sorted(S, key=lambda s: [X.index(c) for c in s])
    # Output
    for s in S:
        print(s)

=======
Suggestion 9

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    #print(X)
    #print(N)
    #print(S)
    #print(len(S))
    #print(len(S[0]))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[

=======
Suggestion 10

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]

    # print(X)
    # print(N)
    # print(S)

    # Sort the list S using the sorted() function.
    # sorted() returns a new sorted list.
    # https://docs.python.org/3/howto/sorting.html
    # https://docs.python.org/3/library/functions.html#sorted

    # The sorted() function takes a key argument.
    # The key argument specifies a function of one argument that is used to extract a comparison key from each list element.
    # The default value of key is None (compare the elements directly).
    # https://docs.python.org/3/library/functions.html#sorted

    # The sorted() function takes a reverse argument.
    # The reverse argument is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
    # The default value of reverse is False.
    # https://docs.python.org/3/library/functions.html#sorted

    # The sorted() function takes a key argument.
    # The key argument specifies a function of one argument that is used to extract a comparison key from each list element.
    # The default value of key is None (compare the elements directly).
    # https://docs.python.org/3/library/functions.html#sorted

    # The sorted() function takes a reverse argument.
    # The reverse argument is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
    # The default value of reverse is False.
    # https://docs.python.org/3/library/functions.html#sorted

    # The sorted() function takes a key argument.
    # The key argument specifies a function of one argument that is used to extract a comparison key from each list element.
    # The default value of key is None (compare the elements directly).
    # https://docs.python.org/3/library/functions.html#sorted

    # The sorted() function takes a reverse argument.
    # The reverse argument is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
    # The default value of reverse is False.
    # https://docs.python.org/3/library/functions.html#sorted

    # The sorted() function takes a key argument.
    # The key argument specifies a function of one
