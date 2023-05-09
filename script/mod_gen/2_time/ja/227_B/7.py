def main():
    n = int(input())
    s = list(map(int,input().split()))
    count = 0
    for i in range(n):
        a = (s[i]-1)//3
        b = (s[i]-a*3)//4
        if s[i] != 4*a*b+3*a+3*b:
            count += 1
    print(count)

if __name__ == '__main__':
    main()