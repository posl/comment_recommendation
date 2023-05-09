def main():
    a, b, x = map(int, input().split())
    if a*10**9 + b*10 < x:
        print(10**9)
    else:
        if a*10**9 + b*1 > x:
            print(0)
        else:
            for i in range(2, 10**9):
                if a*i + b*len(str(i)) > x:
                    print(i-1)
                    break

if __name__ == '__main__':
    main()