def main():
    a, n = map(int, input().split())
    if a == 1:
        print(n)
        return
    x = 1
    for i in range(1, 10**6):
        x = x * a
        if x >= n:
            print(i)
            return
    print(-1)
main()
