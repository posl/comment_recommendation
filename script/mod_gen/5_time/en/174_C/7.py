def main():
    k = int(input())
    if k%2 == 0 or k%5 == 0:
        print(-1)
    else:
        i = 1
        num = 7%k
        while num != 0:
            num = (num*10 + 7)%k
            i += 1
        print(i)

if __name__ == '__main__':
    main()