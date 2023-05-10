def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    for i in range(1, k + 1):
        if i % k == 0:
            print(i)
            return

if __name__ == '__main__':
    main()