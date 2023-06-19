def main():
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        if i%15 == 0:
            pass
        elif i%3 == 0:
            sum = sum + i
        elif i%5 == 0:
            sum = sum + i
        else:
            sum = sum + i
    print(sum)

if __name__ == '__main__':
    main()