def main():
    N = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            count += 1
            a[i] = int(a[i] / 2)
    
    print(count)

if __name__ == '__main__':
    main()