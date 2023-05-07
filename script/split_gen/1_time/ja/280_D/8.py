def main():
    k = int(input())
    n = 1
    while True:
        if n % k == 0:
            print(n)
            break
        n += 1
