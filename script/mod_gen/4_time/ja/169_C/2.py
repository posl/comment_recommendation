def main():
    a,b = map(str,input().split())
    a = int(a)
    b = float(b)
    b = int(b*100)
    ans = a*b
    ans = ans//100
    print(ans)

if __name__ == '__main__':
    main()