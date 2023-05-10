def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    if k % 5 == 0:
        print(-1)
        return
    if k % 7 == 0:
        print(-1)
        return
    if k == 1:
        print(1)
        return
    if k == 3:
        print(3)
        return
    if k == 9:
        print(9)
        return
    n = 1
    while True:
        if int('7' * n) % k == 0:
            print(n)
            return
        n += 1
