def rotate(s):
    s_new = []
    for i in range(len(s)):
        s_new.append([])
        for j in range(len(s)):
            s_new[i].append(s[j][len(s)-1-i])
    return s_new

if __name__ == '__main__':
    rotate()