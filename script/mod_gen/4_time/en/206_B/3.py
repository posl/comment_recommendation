def main():
    N = int(input())
    #print(N)
    sum = 0
    for i in range(1, N+1):
        sum = sum + i
        if sum >= N:
            print(i)
            break
main()

if __name__ == '__main__':
    main()