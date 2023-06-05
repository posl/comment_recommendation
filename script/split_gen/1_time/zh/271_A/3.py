def convert_to_hexadecimal(n):
    if n < 10:
        return str(n)
    elif 10 <= n <= 15:
        return chr(ord('A') + n - 10)
    else:
        return chr(ord('A') + n // 16 - 10) + convert_to_hexadecimal(n % 16)
