def main():
    N = int(input())
    A = list(map(int, input().split()))
    xor = 0
    for a in A:
        xor ^= a
    if xor == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()