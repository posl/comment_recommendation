def main():
    # Read the input
    n, k = map(int, input().split())
    s = input()
    # Print the output
    print(s[:k-1] + s[k-1].lower() + s[k:])
main()
