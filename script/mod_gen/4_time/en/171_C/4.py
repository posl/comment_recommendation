def convert_to_26(n):
    if n < 26:
        return chr(ord('a') + n)
    else:
        return convert_to_26(n // 26 - 1) + convert_to_26(n % 26)
N = int(input())
print(convert_to_26(N - 1))

if __name__ == '__main__':
    convert_to_26()