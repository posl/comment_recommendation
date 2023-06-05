def get_min_count(s):
    if s == s[::-1]: return 0
    if len(s) == 1: return 1
    count = 0
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            count += 1
    return count

if __name__ == '__main__':
    get_min_count()