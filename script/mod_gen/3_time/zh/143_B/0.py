def main():
    N = int(input())
    d = list(map(int,input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1,N):
            sum += d[i]*d[j]
    print(sum)

if __name__ == '__main__':
    main()