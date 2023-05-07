def main():
    N = int(input())
    for i in range(2**60):
        if i & N == i:
            print(i)

if __name__ == '__main__':
    main()