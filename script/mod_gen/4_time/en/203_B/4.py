def main():
    n,k = map(int, input().split())
    count = 0
    for i in range(n):
        for j in range(k):
            count += int(str(i+1) + '0' + str(j+1))
    print(count)

if __name__ == '__main__':
    main()