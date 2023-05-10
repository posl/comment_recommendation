def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
    else:
        i = 1
        v = 7
        while v % k != 0:
            v = (v * 10 + 7) % k
            i += 1
        print(i)

if __name__ == '__main__':
    main()