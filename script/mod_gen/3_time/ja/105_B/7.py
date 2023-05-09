def main():
    n = int(input())
    flag = False
    for i in range(n+1):
        if i*4 + (n-i)*7 == n:
            flag = True
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()