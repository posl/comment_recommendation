def main():
    n = int(input())
    i = 1
    count = 0
    while n >= 1000:
        count += i * (n - 999)
        n //= 1000
        i += 1
    print(count)
