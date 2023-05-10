def main():
    n = int(input())
    aoki = 0
    takahashi = 0
    for i in range(1, 2*n+2):
        print(i)
        aoki = int(input())
        if aoki == 0:
            break
        takahashi = i
    exit()

if __name__ == '__main__':
    main()