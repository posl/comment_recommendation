def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))
    #process
    a.sort(reverse=True)
    max_even = -1
    for i in range(n):
        if a[i] % 2 == 0:
            max_even = a[i]
            break
    if max_even == -1:
        print(-1)
        exit()
    for i in range(n):
        if a[i] % 2 == 0 and a[i] < max_even * 2:
            print(max_even)
            exit()
    print(-1)

if __name__ == '__main__':
    main()