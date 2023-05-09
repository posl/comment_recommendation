def count_diff_chars(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

if __name__ == '__main__':
    count_diff_chars()