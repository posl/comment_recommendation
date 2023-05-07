def main():
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        if i%3==0 and i%5==0:
            continue
        elif i%3==0 or i%5==0:
            continue
        else:
            sum += i
    print(sum)

if __name__ == '__main__':
    main()