def count_abc(s):
    count = 0
    for i in range(0, len(s)):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

if __name__ == '__main__':
    count_abc()