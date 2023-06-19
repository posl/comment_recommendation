def main():
    s,t = input().split()
    a,b = input().split()
    u = input()
    a = int(a)
    b = int(b)
    if s == u:
        a = a - 1
    else:
        b = b - 1
    print(a,b)

if __name__ == '__main__':
    main()