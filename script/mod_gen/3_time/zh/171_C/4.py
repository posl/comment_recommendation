def get_name(number):
    name = ''
    if number <= 26:
        name = chr(number + 96)
    else:
        name = get_name(number // 26) + get_name(number % 26)
    return name
n = int(input())
print(get_name(n))
