def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        exit()
    mod = 7 % k
    for i in range(1, k+1):
        if mod == 0:
            print(i)
            exit()
        mod = (mod * 10 + 7) % k
    print(-1)
main()

if __name__ == '__main__':
    main()