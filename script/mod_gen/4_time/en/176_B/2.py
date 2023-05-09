def main():
    N = input()
    while len(N) > 1:
        N = str(sum([int(i) for i in N]))
    if int(N) % 9 == 0:
        print('Yes')
    else:
        print('No')
main()
Code 2

if __name__ == '__main__':
    main()