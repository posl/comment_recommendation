def main():
    s,t = input().split()
    a,b = map(int,input().split())
    u = input()
    if s == u:
        a -= 1
    elif t == u:
        b -= 1
    print(a,b)
main()

if __name__ == '__main__':
    main()