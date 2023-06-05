def main():
    n = input()
    k = len(n)
    if k == 1:
        if int(n) % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    else:
        for i in range(1, k):
            for j in range(k):
                if i + j <= k:
                    if int(n[j:j + i]) % 3 == 0:
                        print(k - i)
                        return
    print(-1)

if __name__ == '__main__':
    main()