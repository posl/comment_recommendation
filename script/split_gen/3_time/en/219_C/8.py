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
