def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
    else:
        n = 7
        for i in range(1, k+1):
            if n % k == 0:
                print(i)
                break
            else:
                n = (n * 10 + 7) % k
        else:
            print(-1)

if __name__ == '__main__':
    main()