def main():
    k = int(input().rstrip())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    r = 1
    for i in range(1, k+1):
        r = (r * 10 + 7) % k
        if r == 0:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()