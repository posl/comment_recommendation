def convert(num):
    if num == 0:
        return ""
    else:
        return convert((num - 1) // 26) + chr((num - 1) % 26 + ord("a"))
n = int(input())
print(convert(n))
