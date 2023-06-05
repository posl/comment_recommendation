def main():
    n = int(input())
    ds = list(map(int, input().split()))
    ds.sort()
    #print(ds)
    left = ds[n//2-1]
    right = ds[n//2]
    print(right-left)

if __name__ == '__main__':
    main()