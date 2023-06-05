def main():
    n = int(input())
    a = [0] * 100
    i = 0
    while n > 0:
        a[i] = n % 26
        if a[i] == 0:
            a[i] = 26
            n = n // 26 - 1
        else:
            n = n // 26
        i += 1
    for j in range(i - 1, -1, -1):
        print(chr(ord('a') + a[j] - 1), end='')
    print()
