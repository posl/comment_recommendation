def change(a,b,s):
    s = list(s)
    s[a-1],s[b-1] = s[b-1],s[a-1]
    return "".join(s)

if __name__ == '__main__':
    change()