def main():
    K = int(input())
    for i in range(K):
        print(chr(ord('A') + i), end='')
    print()

if __name__ == '__main__':
    main()