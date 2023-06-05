def count_bottom(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            count += s[i:].count('w')
    return count

if __name__ == '__main__':
    count_bottom()