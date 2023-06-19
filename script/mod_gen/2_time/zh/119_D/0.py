def search(s,t,x):
    i = 0
    j = 0
    while i < len(s) and s[i] < x:
        i += 1
    while j < len(t) and t[j] < x:
        j += 1
    if i == 0:
        return t[j] - x
    elif j == 0:
        return s[i] - x
    else:
        return min(s[i] - x + s[i] - t[j-1], t[j] - x + t[j] - s[i-1], s[i] - x + t[j] - x, s[i] - x + t[j] - x)

if __name__ == '__main__':
    search()