def main():
    N = int(input())
    a = 2
    b = 2
    count = 0
    while a <= N:
        while b <= N:
            if a ** b <= N:
                count += 1
            b += 1
        a += 1
        b = 2
    print(N - count)
