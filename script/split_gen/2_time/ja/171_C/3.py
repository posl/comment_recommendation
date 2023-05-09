def get_alphabet(n):
    if n <= 26:
        return chr(ord('a') + n - 1)
    else:
        return get_alphabet((n-1) // 26) + get_alphabet((n-1) % 26 + 1)
n = int(input())
print(get_alphabet(n))
