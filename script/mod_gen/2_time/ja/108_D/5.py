def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    print(L+1, L+1)
    for i in range(L+1):
        print(i+1, i+2, 0)
    for i in range(L):
        print(i+1, i+2, 1)
    print(L+1, 1, L-1)

if __name__ == '__main__':
    main()