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

if __name__ == '__main__':
    main()