def main():
    n = int(input())
    min_time = 10**5*2
    for i in range(n):
        a,b = map(int,input().split())
        if a+b < min_time:
            min_time = a+b
    print(min_time)

if __name__ == '__main__':
    main()