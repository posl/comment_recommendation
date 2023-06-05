def swap(s, i, j):
    if i > j:
        i, j = j, i
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
