def convert(s, base):
    x = 0
    for i in s:
        x = x * base + int(i)
    return x

if __name__ == '__main__':
    convert()