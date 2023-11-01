def countRGB(s):
    count = 0
    for i in range(len(s)-2):
        for j in range(i+1, len(s)-1):
            k = j + j - i
            if k < len(s) and s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                count += 1
    return count

if __name__ == '__main__':
    countRGB()