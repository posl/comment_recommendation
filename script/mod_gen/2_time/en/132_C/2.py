def main():
    #input
    N = int(input())
    ds = input().split()
    for i in range(N):
        ds[i] = int(ds[i])
    #sort
    ds = sorted(ds)
    #output
    print(ds[N//2]-ds[N//2-1])

if __name__ == '__main__':
    main()