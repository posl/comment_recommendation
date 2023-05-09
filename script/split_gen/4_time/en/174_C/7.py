def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    n = 7 % k
    for i in range(1, 10**6 + 1):
        if n == 0:
            print(i)
            return
        n = (n * 10 + 7) % k
    print(-1)
