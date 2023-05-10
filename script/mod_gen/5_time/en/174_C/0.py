def main():
    k = int(input())
    x = 7 % k
    for i in range(k):
        if x == 0:
            print(i + 1)
            return
        x = (x * 10 + 7) % k
    print(-1)
main()

if __name__ == '__main__':
    main()