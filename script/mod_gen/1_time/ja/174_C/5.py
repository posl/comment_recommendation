def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    i = 1
    mod = 7 % K
    while mod != 0:
        mod = (mod * 10 + 7) % K
        i += 1
    print(i)

if __name__ == '__main__':
    main()