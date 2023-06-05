def main():
    n = int(input())
    result = 0
    for i in range(n):
        a,b = map(int,input().split())
        result += (b-a+1)*(a+b)/2
    print(int(result))

if __name__ == '__main__':
    main()