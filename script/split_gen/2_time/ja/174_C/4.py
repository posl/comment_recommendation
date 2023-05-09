def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    n = 1
    while 7 % k != 0:
        n += 1
        7 = 7 * 10 + 7
    print(n)
