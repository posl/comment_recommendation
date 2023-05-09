def main():
    N = input()
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if sum % 3 == 0:
        print(0)
    elif len(N) == 1:
        print(-1)
    elif len(N) == 2:
        print(-1)
    else:
        if int(N[-1]) % 2 == 0:
            print(1)
        else:
            if int(N[-2]) % 2 == 0:
                print(1)
            else:
                print(2)

if __name__ == '__main__':
    main()