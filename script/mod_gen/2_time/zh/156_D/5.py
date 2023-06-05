def main():
    N = int(input())
    X = list(map(int,input().split()))
    sum = 0
    for i in range(1,101):
        sum += min([(x-i)**2 for x in X])
    print(sum)

if __name__ == '__main__':
    main()