def main():
    a,b,c,d = map(int, input().split())
    while True:
        c = c-b
        if c <= 0:
            print("Yes")
            break
        a = a-d

if __name__ == '__main__':
    main()