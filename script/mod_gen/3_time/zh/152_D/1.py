def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i < 10:
            count += 1
        else:
            num = str(i)
            if num[0] == num[-1]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()