def main():
    # get input
    k = int(input())
    # get even and odd numbers
    even = k // 2
    odd = k // 2 + k % 2
    print(even * odd)

if __name__ == '__main__':
    main()