def count_ABCs(s):
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == 'ABC':
            count += 1
    return count

if __name__ == '__main__':
    count_ABCs()