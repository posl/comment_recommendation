def main():
    n,m = map(int,input().split())
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        sum = sum + a*b
    print(sum//m)

if __name__ == '__main__':
    main()