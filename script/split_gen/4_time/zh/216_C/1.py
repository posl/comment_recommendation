def main():
    n = int(input())
    s = []
    while n > 0:
        if n % 2 == 0:
            s.append('B')
            n = int(n/2)
        else:
            s.append('A')
            n -= 1
    s.reverse()
    print(''.join(s))
