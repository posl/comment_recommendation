def main():
    N = input()
    while len(N) > 1:
        N = str(sum(map(int, list(N))))
    print('Yes' if N == '9' else 'No')
main()

if __name__ == '__main__':
    main()