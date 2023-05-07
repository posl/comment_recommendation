def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    a = 7 % K
    for i in range(1, 10**6+1):
        if a == 0:
            print(i)
            return
        a = (a * 10 + 7) % K
    print(-1)

if __name__ == '__main__':
    main()