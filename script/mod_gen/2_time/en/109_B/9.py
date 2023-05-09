def main():
    # Read the input
    n = int(input())
    words = [input() for _ in range(n)]
    # Check if the shiritori rules were observed
    if len(set(words)) == n and all(words[i][0] == words[i-1][-1] for i in range(1, n)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()