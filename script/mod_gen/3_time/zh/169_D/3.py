def main():
    n = int(input())
    z = 2
    cnt = 0
    while n > 1:
        if n % z == 0:
            n = n // z
            cnt += 1
        else:
            z += 1
    print(cnt)

if __name__ == '__main__':
    main()