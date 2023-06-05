def main():
    n = input()
    k = len(n)
    n = int(n)
    if n % 3 == 0:
        print(0)
        return
    for i in range(k):
        n = n // 10
        k -= 1
        if n % 3 == 0:
            print(k)
            return
    print(-1)
