def main():
    K = int(input())
    m = 1
    for i in range(1, K+1):
        m *= i
        if m % K == 0:
            print(i)
            exit()
    print(K)

if __name__ == '__main__':
    main()