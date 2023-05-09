def main():
    N = int(input())
    day = 0
    for i in range(1, N+1):
        day += i
        if day >= N:
            print(i)
            break

if __name__ == '__main__':
    main()