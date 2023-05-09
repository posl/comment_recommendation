def main():
    N = int(input())
    s = ''
    while N > 0:
        if N % 2 == 0:
            s = 'B' + s
            N = N // 2
        else:
            s = 'A' + s
            N -= 1
    print(s)
