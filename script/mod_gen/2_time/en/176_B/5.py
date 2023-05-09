def main():
    N = input()
    while len(N) > 1:
        N = str(sum([int(x) for x in N]))
    if N == '9':
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()