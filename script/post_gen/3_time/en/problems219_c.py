Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda s: [X.index(c) for c in s])
    for s in S:
        print(s)

=======
Suggestion 2

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=lambda x: [X.index(c) for c in x])
    for s in S:
        print(s)

main()

=======
Suggestion 3

def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort(key=lambda x: [X.index(c) for c in x])
    for s in S:
        print(s)

=======
Suggestion 4

def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort(key = lambda x: [X.index(c) for c in x])
    for i in range(N):
        print(S[i])

=======
Suggestion 5

def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    s = sorted(s, key=lambda x: [x.index(c) for c in x])
    for i in s:
        print(i)

=======
Suggestion 6

def get_key(s):
    return [key.index(c) for c in s]

key = input()
N = int(input())
S = [input() for _ in range(N)]

for s in sorted(S, key=get_key):
    print(s)

import sys
from collections import defaultdict
from itertools import permutations

=======
Suggestion 7

def main():
    #read input
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    #sort S
    S.sort(key=lambda s: [X.index(c) for c in s])
    #print output
    for s in S:
        print(s)

=======
Suggestion 8

def main():
    # read data
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # sort data
    sorted_S = sorted(S, key=lambda x: [X.index(c) for c in x])
    # output
    for s in sorted_S:
        print(s)

=======
Suggestion 9

def main():
    # Get the input
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    # Sort the list S based on the new alphabetical order
    S.sort(key=lambda x: [X.index(c) for c in x])
    # Print the list
    for s in S:
        print(s)

=======
Suggestion 10

def main():
    # Read the input
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # Create a dictionary to map the new alphabetical order to the old one
    X_map = {X[i]: chr(ord('a')+i) for i in range(26)}
    # Create a new list of names that are mapped to the new alphabetical order
    S_new = []
    for name in S:
        name_new = []
        for char in name:
            name_new.append(X_map[char])
        S_new.append(''.join(name_new))
    # Sort the list of names lexicographically
    S_new.sort()
    # Map the sorted names back to the old alphabetical order
    S_sorted = []
    for name in S_new:
        name_sorted = []
        for char in name:
            name_sorted.append(X[ord(char)-ord('a')])
        S_sorted.append(''.join(name_sorted))
    # Print the sorted list of names
    for name in S_sorted:
        print(name)

main()
