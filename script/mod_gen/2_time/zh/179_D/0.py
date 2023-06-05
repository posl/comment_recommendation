def main():
    n = int(input())
    count = 0
    for i in range(1,n):
        for j in range(i,n):
            if i*j < n:
                count += 1
            else:
                break
    print(count)

if __name__ == '__main__':
    main()