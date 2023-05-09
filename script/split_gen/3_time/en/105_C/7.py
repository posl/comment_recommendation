def main():
    n = int(input())
    if n == 0:
        print(0)
    else:
        s = ''
        while n:
            if n % (-2) == 0:
                s = '0' + s
                n //= (-2)
            else:
                s = '1' + s
                n = (n - 1) // (-2)
        print(s)
