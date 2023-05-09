def main():
    #input
    N = int(input())
    Ps = list(map(int,input().split()))
    #count
    count = 0
    min = N+1
    for i in range(N):
        if Ps[i] < min:
            count += 1
            min = Ps[i]
    #output
    print(count)
main()

if __name__ == '__main__':
    main()