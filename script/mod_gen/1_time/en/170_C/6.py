def main():
    x, n = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]
    p.sort()
    if n == 0:
        print(x)
    else:
        for i in range(0, 101):
            if x-i not in p:
                print(x-i)
                break
            elif x+i not in p:
                print(x+i)
                break
main()

if __name__ == '__main__':
    main()