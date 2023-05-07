def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        print(0)
        return
    for i in range(1, N):
        if a[i] == a[i-1]:
            print(i)
            return
    print(N)

if __name__ == '__main__':
    main()