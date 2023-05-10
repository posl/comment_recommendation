def century(n):
    if n % 100 == 0:
        return n // 100
    else:
        return n // 100 + 1
n = int(input())
print(century(n))

if __name__ == '__main__':
    century()