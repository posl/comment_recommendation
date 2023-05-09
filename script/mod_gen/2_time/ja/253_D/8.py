def main():
    n,a,b = map(int,input().split())
    #print(n,a,b)
    #print(n//a + n//b - n//lcm(a,b))
    print(n - n//a - n//b + n//lcm(a,b))

if __name__ == '__main__':
    main()