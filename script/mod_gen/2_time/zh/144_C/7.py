def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i*i > n:
            break
        if n % i == 0:
            count += 1
    print(count*2)

if __name__ == '__main__':
    main()