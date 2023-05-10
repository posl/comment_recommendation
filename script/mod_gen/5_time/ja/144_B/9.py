def main():
    n = int(input())
    flag = False
    for i in range(1,10):
        if n % i == 0 and n//i < 10:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()