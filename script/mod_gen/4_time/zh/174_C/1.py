def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        exit(0)
    else:
        for i in range(1, K+1):
            if int(str(7)*i) % K == 0:
                print(i)
                exit(0)

if __name__ == '__main__':
    main()