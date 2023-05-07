def convert(n):
    if n < 27:
        return chr(ord('a') + n - 1)
    else:
        return convert((n - 1) // 26) + convert((n - 1) % 26 + 1)
N = int(input())
print(convert(N))

if __name__ == '__main__':
    convert()