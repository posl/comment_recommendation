def main():
    D, T, S = map(int, input().split())
    if D / S <= T:
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()