Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    print('

'.join(sorted(S, key=lambda s: [X.index(c) for c in s])))

=======
Suggestion 2

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    d = {c:i for i, c in enumerate(X)}
    S.sort(key=lambda s:[d[c] for c in s])
    for s in S:
        print(s)

=======
Suggestion 3

def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort(key=lambda x: [x.index(c) for c in x if c in x])
    for i in range(n):
        print(s[i])

=======
Suggestion 4

def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort(key=lambda x: [x.index(i) for i in x if i in x])
    print('

'.join(s))

=======
Suggestion 5

def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort(key=lambda e: [x.index(c) for c in e])
    print(*s, sep='

')

=======
Suggestion 6

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]

    new_order = {c: i for i, c in enumerate(X)}
    S.sort(key=lambda s: [new_order[c] for c in s])
    print(*S, sep='

')

=======
Suggestion 7

def main():
    X = input()
    N = int(input())
    
    S = []
    for i in range(N):
        S.append(input())
        
    S.sort(key=lambda x: [X.index(c) for c in x])
    
    for i in range(N):
        print(S[i])

=======
Suggestion 8

def main():
    # read the input
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # sort the names
    S.sort(key=lambda s: [X.index(c) for c in s])
    # print the sorted names
    for s in S:
        print(s)

=======
Suggestion 9

def main():
    # Read the alphabet
    alphabet = input()
    # Read the number of names
    n = int(input())
    # Read the names
    names = []
    for _ in range(n):
        name = input()
        names.append(name)
    # Sort the names
    names.sort(key=lambda name: [alphabet.index(c) for c in name])
    # Print the sorted names
    for name in names:
        print(name)

=======
Suggestion 10

def main():
    # Read the input
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    
    # Convert the new alphabetical order to a dictionary
    d = {c:i for i, c in enumerate(X)}
    
    # Sort the names lexicographically
    S.sort(key=lambda s: [d[c] for c in s])
    
    # Print the sorted names
    for s in S:
        print(s)

main()
