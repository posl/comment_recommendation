def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = (n-1)//min(a, b, c, d, e) + 5
    print(ans)

if __name__ == '__main__':
    main()