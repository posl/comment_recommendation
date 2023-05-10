def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j > n:
                break
            else:
                count += 1
    print(count)

if __name__ == '__main__':
    main()