def main():
    k = int(input())
    #print(k)
    n = 1
    while True:
        if (n % k == 0):
            print(n)
            break
        n += 1

if __name__ == '__main__':
    main()