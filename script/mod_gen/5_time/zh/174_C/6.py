def main():
    k = int(input())
    num = 7
    for i in range(1, k+1):
        if num % k == 0:
            print(i)
            break
        else:
            num = num * 10 + 7
    else:
        print(-1)

if __name__ == '__main__':
    main()