def get_letter(num):
    letter = ''
    while num > 0:
        num -= 1
        letter = chr(97 + num % 26) + letter
        num = num // 26
    return letter
num = int(input())
print(get_letter(num))
