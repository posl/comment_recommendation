def main():
    N = int(input())
    if N % 2 == 0:
        print(0.5)
    else:
        print((N//2+1)/N)
main()

if __name__ == '__main__':
    main()