Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    print(len(S))

=======
Suggestion 3

def main():
    # Get the number of times to draw
    num_draws = int(input())
    # Create a set to store the items
    items = set()
    # Iterate through the draws
    for i in range(num_draws):
        # Get the item from the draw
        item = input()
        # Add the item to the set
        items.add(item)
    # Print the number of unique items
    print(len(items))

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    s.sort()
    count = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 6

def problems164_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    print(len(s))

problems164_c()
