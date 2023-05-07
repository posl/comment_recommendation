def main():
    N = int(input())
    count = 0
    for i in range(2,10**6):
        if N%i == 0:
            count += 1
            N = N//i
            i = 1
    print(count)

if __name__ == '__main__':
    main()