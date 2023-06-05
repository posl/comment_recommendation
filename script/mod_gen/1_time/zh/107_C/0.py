def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    time = 0
    for i in range(k):
        if x[i] < 0:
            time += abs(x[i])
            if x[i+1] < 0:
                time += abs(x[i+1])
            else:
                time += x[i+1]
        else:
            time += x[i]
    print(time)

if __name__ == '__main__':
    main()