def main():
    k = int(input())
    n = 1
    while True:
        if (n % k) == 0:
            break
        else:
            n += 1
    print(n)
