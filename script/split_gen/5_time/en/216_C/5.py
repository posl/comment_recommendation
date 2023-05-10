def main():
    n = int(input())
    s = []
    while n > 0:
        if n % 2 == 0:
            s.append('B')
            n = n // 2
        else:
            s.append('A')
            n -= 1
    print(''.join(s[::-1]))
