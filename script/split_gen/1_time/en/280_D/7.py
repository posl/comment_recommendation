def main():
    k = int(input())
    n = k
    for i in range(2, 100000):
        if n % i == 0:
            n = n // i
            i = 1
        if n == 1:
            print(i)
            exit()
