def main():
    N = int(input())
    print(N%100)
    if N%100 == 0:
        print(N//100)
    else:
        print(N//100 + 1)

if __name__ == '__main__':
    main()