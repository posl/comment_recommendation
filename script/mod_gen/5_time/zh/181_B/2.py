def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        sum += (b-a+1)*(a+b)/2
    print(int(sum))

if __name__ == '__main__':
    main()