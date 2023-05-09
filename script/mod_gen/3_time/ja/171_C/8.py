def calc(n):
    if n == 0:
        return ""
    elif n <= 26:
        return chr(96+n)
    else:
        if n % 26 == 0:
            return calc(n//26-1) + chr(122)
        else:
            return calc(n//26) + chr(96+n%26)
n = int(input())
print(calc(n))

if __name__ == '__main__':
    calc()