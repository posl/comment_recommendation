def swap(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count += i
        elif s[i] > 'a':
            count += i
            s = s[:i] + 'a' + s[i+1:]
    return count

if __name__ == '__main__':
    swap()