def count_d(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += s.count('v', i+1, len(s))
    return count

if __name__ == '__main__':
    count_d()