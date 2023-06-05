def main():
    n,x = input().split(" ")
    n = int(n)
    x = int(x)
    p = input().split(" ")
    for i in range(n):
        p[i] = int(p[i])
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break

if __name__ == '__main__':
    main()