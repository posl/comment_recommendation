def main():
    #input
    N = int(input())
    a = list(map(int, input().split()))
    #process
    cnt = 0
    for i in range(N):
        while True:
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
                cnt += 1
            else:
                break
    #output
    print(cnt)

if __name__ == '__main__':
    main()