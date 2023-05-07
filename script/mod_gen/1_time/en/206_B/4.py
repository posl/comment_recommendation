def main():
    N = int(input())
    x = 0
    for i in range(N):
        x += i
        if x >= N:
            print(i)
            break

if __name__ == '__main__':
    main()