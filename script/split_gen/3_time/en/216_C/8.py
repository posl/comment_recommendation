def main():
    N = int(input())
    s = ''
    while N > 0:
        if N % 2 == 1:
            N -= 1
            s += 'A'
        else:
            N //= 2
            s += 'B'
    print(s[::-1])
