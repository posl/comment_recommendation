def main():
    K = int(input())
    n = 2
    while True:
        if K % n == 0:
            print(n)
            break
        else:
            n += 1
