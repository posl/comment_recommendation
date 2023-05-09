def main():
    n = int(input())
    for i in range(1, n+1):
        if (7 * i) % n == 0:
            print(i)
            exit()
    print(-1)
