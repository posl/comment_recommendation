def main():
    N = int(input())
    X = list(map(int, input().split()))
    min = 100000000
    for i in range(1,101):
        sum = 0
        for j in range(0,N):
            sum += (X[j]-i)**2
        if sum < min:
            min = sum
    print(min)

if __name__ == '__main__':
    main()