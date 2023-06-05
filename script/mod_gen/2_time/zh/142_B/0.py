def main():
    N = int(input())
    a = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            a += 1
    print(a/N)

if __name__ == '__main__':
    main()