def main():
    n = int(input())
    a = 0
    while n >= 1000:
        n = n // 1000
        a += 1
    print(a)
