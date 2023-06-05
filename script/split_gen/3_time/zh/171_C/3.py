def main():
    N = int(input())
    s = ''
    while N > 0:
        N -= 1
        s = chr(ord('a') + N % 26) + s
        N //= 26
    print(s)
