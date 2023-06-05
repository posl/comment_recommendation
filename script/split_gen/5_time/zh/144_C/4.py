def main():
    n = int(input())
    a = int(n ** 0.5)
    while n % a != 0:
        a -= 1
    print(a + n // a - 2)
