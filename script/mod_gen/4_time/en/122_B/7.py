def longest_acgt(s):
    longest = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_acgt(s[i:j+1]):
                longest = max(longest, j-i+1)
    return longest

if __name__ == '__main__':
    longest_acgt()