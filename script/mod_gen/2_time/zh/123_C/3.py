def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_abcde = min(a,b,c,d,e)
    if n <= min_abcde:
        print(5)
    else:
        print(5 + (n - min_abcde - 1)//min_abcde + 1)

if __name__ == '__main__':
    main()