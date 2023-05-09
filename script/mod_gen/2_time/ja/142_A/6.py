def main():
    N = int(input())
    # N = 4
    # N = 5
    # N = 1
    odd = 0
    for i in range(1,N+1):
        if i % 2 == 1:
            odd += 1
    print(odd/N)

if __name__ == '__main__':
    main()