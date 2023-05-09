def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    result = []
    while n != 0:
        if n % 2 == 0:
            result.append(0)
            n = n // (-2)
        else:
            result.append(1)
            n = (n - 1) // (-2)
    result.reverse()
    print(''.join(map(str, result)))
