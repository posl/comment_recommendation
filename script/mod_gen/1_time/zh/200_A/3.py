def main():
    N = int(input())
    century = N//100
    if N%100 != 0:
        century += 1
    print(century)

if __name__ == '__main__':
    main()