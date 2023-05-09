def convert(n):
    if n < 27:
        return chr(96+n)
    else:
        return convert((n-1)//26) + chr(96 + n%26 + 1)
N = int(input())
print(convert(N))

if __name__ == '__main__':
    convert()