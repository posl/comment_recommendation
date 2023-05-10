def permutation_lexicographically_smallest(string, k):
    # Count the frequency of each character
    freq = [0] * 26
    for c in string:
        freq[ord(c) - ord('a')] += 1
    # Find the lexicographically smallest permutation
    result = []
    for i in range(len(string)):
        for j in range(26):
            if freq[j] == 0:
                continue
            # Remove character j and append it to the result
            freq[j] -= 1
            permutation = "".join([chr(ord('a') + k) * freq[k] for k in range(26)])
            if k <= factorial(len(string) - i - 1):
                result.append(chr(ord('a') + j))
                break
            else:
                k -= factorial(len(string) - i - 1)
                freq[j] += 1
    return "".join(result)

if __name__ == '__main__':
    permutation_lexicographically_smallest()