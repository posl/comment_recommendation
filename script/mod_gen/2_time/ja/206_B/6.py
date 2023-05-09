def main():
    N = int(input())
    if N == 1:
        print(1)
    else:
        a = 0
        for i in range(1,N):
            a += i
            if N <= a:
                print(i)
                break

if __name__ == '__main__':
    main()