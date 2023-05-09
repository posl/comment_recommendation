def main():
    n, x = map(int, input().split())
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        print(alpha[int((x-1)/n)], end="")
        x = x%n
        if x==0:
            x=n
    print()

if __name__ == '__main__':
    main()