def main():
    # Enter the number of votes
    n = int(input())
    # Enter the strings
    s = []
    for i in range(n):
        s.append(input())
    # Count the number of votes for each string
    s_count = {}
    for i in range(n):
        if s[i] in s_count:
            s_count[s[i]] += 1
        else:
            s_count[s[i]] = 1
    # Find the string with the most votes
    s_max = max(s_count.values())
    # Print the strings with the most votes
    for key, value in s_count.items():
        if value == s_max:
            print(key)

if __name__ == '__main__':
    main()