def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    if N%2 == 0:
        print(d[int(N/2)] - d[int(N/2)-1])
    else:
        print(0)

if __name__ == '__main__':
    main()