def main():
    k = int(input())
    s = 7
    for i in range(1, k + 1):
        if s % k == 0:
            print(i)
            return
        s = s * 10 + 7
    print(-1)

if __name__ == '__main__':
    main()