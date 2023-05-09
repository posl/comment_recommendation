def main():
    # Read the input
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # Count the number of times each alphabet occurs in each string
    cnts = [Counter(s) for s in S]
    # The answer is the maximum number of distinct alphabets that satisfy the condition
    ans = 0
    # Try all 26 alphabets
    for i in range(26):
        # The alphabet we are trying
        c = chr(ord('a') + i)
        # How many strings contain the alphabet
        num = 0
        # Count the number of strings that contain the alphabet
        for cnt in cnts:
            if cnt[c] > 0:
                num += 1
        # If the number of strings that contain the alphabet is less than K, we cannot use the alphabet
        if num < K:
            continue
        # If the number of strings that contain the alphabet is greater than or equal to K, we can use the alphabet
        # Try all possible combinations of strings that contain the alphabet
        for comb in combinations(cnts, num):
            # Count the number of times the alphabet occurs in the strings
            cnt = Counter()
            for c in comb:
                cnt += c
            # If the alphabet occurs in exactly K of the strings, update the answer
            if cnt[c] == K:
                ans = max(ans, num)
    # Print the answer
    print(ans)

if __name__ == '__main__':
    main()