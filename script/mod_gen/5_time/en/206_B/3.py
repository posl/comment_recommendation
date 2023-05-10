def main():
    n = int(input())
    x = 0
    for i in range(1, 10**9+1):
        x += i
        if x >= n:
            print(i)
            break

if __name__ == '__main__':
    main()