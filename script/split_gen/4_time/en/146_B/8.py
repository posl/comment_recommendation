def shift(s, n):
    return ''.join([chr((ord(c) - 65 + n) % 26 + 65) for c in s])
n = int(input())
s = input()
print(shift(s, n))
In the above code, I have used a list comprehension to shift each character in the input string by n . The ord() function returns the ASCII code of a character and chr() function returns the character for a given ASCII code. The modulo operator ( % ) is used to handle the case where the shifted character is beyond Z , which is equivalent to A .
