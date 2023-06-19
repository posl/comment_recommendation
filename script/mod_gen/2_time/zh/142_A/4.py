def main():
    N = int(input())
    if N%2 == 0:
        print(0.5)
    else:
        print(round((N//2+1)/N, 10))

if __name__ == '__main__':
    main()