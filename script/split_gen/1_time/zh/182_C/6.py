def main():
    n = input()
    k = len(n)
    n = int(n)
    if n % 3 == 0:
        print(0)
        return
    for i in range(1, k):
        for j in range(k - i):
            if int(n / 10 ** j) % 3 == 0:
                print(i)
                return
    print(-1)
