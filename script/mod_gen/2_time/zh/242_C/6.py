def minstring(s):
    s = list(s)
    s.sort()
    return "".join(s)

if __name__ == '__main__':
    minstring()