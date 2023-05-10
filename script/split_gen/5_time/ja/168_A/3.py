def get_honponbon(n):
    honponbon = ""
    if n % 10 == 2 or n % 10 == 4 or n % 10 == 5 or n % 10 == 7 or n % 10 == 9:
        honponbon = "hon"
    elif n % 10 == 0 or n % 10 == 1 or n % 10 == 6 or n % 10 == 8:
        honponbon = "pon"
    elif n % 10 == 3:
        honponbon = "bon"
    return honponbon
n = int(input())
print(get_honponbon(n))
