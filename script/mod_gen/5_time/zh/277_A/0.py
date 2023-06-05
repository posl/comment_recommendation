def main():
    num = input().split()
    num = [int(i) for i in num]
    n = num[0]
    x = num[1]
    p = input().split()
    p = [int(i) for i in p]
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break

if __name__ == '__main__':
    main()