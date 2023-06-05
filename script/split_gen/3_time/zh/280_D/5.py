def main():
    k = int(input())
    n = 1
    while True:
        if k % n == 0:
            print(n)
            break
        else:
            n += 1
