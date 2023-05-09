def main():
    n = int(input())
    s = 0
    for i in str(n):
        s += int(i)
    if s % 9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()