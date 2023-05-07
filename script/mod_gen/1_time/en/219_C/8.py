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

if __name__ == '__main__':
    main()