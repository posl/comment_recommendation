def main():
    n = int(input())
    result = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            result.append('B')
        else:
            n = n - 1
            result.append('A')
    result.reverse()
    print(''.join(result))
