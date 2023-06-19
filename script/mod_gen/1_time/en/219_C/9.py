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
