def base2(num):
    if num == 0:
        return num
    else:
        return num % (-2) + 10 * base2(num // (-2))
num = int(input())
print(base2(num))
