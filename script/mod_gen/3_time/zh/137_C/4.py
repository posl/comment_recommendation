def count(s):
    result = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                result += 1
    return result

if __name__ == '__main__':
    count()