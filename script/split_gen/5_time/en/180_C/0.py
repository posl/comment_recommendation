def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i * i != n:
                print(n // i)
        i += 1
