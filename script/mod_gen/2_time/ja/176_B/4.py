def main():
    N = input()
    N = int(N)
    N = str(N)
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()