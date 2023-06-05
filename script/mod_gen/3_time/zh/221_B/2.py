def swap(i, j, s):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)
s = input()
t = input()

if __name__ == '__main__':
    swap()