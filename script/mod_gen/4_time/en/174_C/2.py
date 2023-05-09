def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        i = 1
        num = 7
        while num % K != 0:
            num = (num * 10 + 7) % K
            i += 1
        print(i)

if __name__ == '__main__':
    main()