def main():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if int(n) % sum == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()