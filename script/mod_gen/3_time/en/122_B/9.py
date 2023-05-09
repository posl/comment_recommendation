def get_longest_ACGT_string(s):
    longest_length = 0
    current_length = 0
    for c in s:
        if c in ['A', 'C', 'G', 'T']:
            current_length += 1
        else:
            longest_length = max(longest_length, current_length)
            current_length = 0
    return max(longest_length, current_length)

if __name__ == '__main__':
    get_longest_ACGT_string()