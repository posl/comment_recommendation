def main():
    k = int(input())
    a = 7
    for i in range(1, k+1):
        if a % k == 0:
            print(i)
            return
        a = (a * 10 + 7) % k
    print(-1)

if __name__ == '__main__':
    main()