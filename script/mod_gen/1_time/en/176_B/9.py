def main():
    N = input().strip()
    if sum(int(n) for n in N) % 9 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()