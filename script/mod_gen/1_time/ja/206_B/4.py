def main():
    n = int(input())
    sum = 0
    count = 0
    while(sum < n):
        count += 1
        sum += count
    print(count)

if __name__ == '__main__':
    main()