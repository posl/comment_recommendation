def main():
    n,x = map(int,input().split())
    data = []
    for i in range(n):
        data.append(list(map(int,input().split())))
    print(data)
    min_time = 10**9*n
    for i in range(1,n+1):
        sum_time = 0
        for j in range(n):
            if j == i-1:
                sum_time += data[j][0]+data[j][1]
            else:
                sum_time += data[j][1]
        if sum_time < min_time:
            min_time = sum_time
    print(min_time+x)

if __name__ == '__main__':
    main()