def main():
    n = int(input())
    x = 7
    for i in range(1, n+1):
        if x % n == 0:
            print(i)
            exit()
        else:
            x = x*10 + 7
    print(-1)
