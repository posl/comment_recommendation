def main():
    n = int(input())
    if n == 0:
        print(0)
    else:
        s = []
        while n != 0:
            if n % 2 == 0:
                s.append('0')
                n = n // -2
            else:
                s.append('1')
                n = (n - 1) // -2
        print(''.join(s[::-1]))
