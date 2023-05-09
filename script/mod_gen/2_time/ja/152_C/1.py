def main():
    n = int(input())
    p = list(map(int,input().split()))
    count = 1
    min_p = p[0]
    for i in range(1,n):
        if p[i] <= min_p:
            min_p = p[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()