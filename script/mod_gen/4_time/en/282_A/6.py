def main():
    k = int(input())
    for i in range(k):
        print(chr(ord('A')+i),end='')
    print()

if __name__ == '__main__':
    main()