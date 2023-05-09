def round(num, n):
    if num % (10 ** n) == 0:
        return num
    else:
        return round(num + 10 ** n - num % (10 ** n), n)
x, k = map(int, input().split())
print(round(x, k))

if __name__ == '__main__':
    round()