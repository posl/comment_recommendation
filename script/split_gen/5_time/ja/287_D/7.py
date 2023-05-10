def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    for i in range(n - m + 1):
        if all(s[i + j] == t[j] or s[i + j] == '?' for j in range(m)):
            print('Yes')
        else:
            print('No')
