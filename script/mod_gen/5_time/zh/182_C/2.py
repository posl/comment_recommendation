def main():
    n = int(input())
    if n % 3 == 0:
        print(0)
        return
    s = str(n)
    k = len(s)
    for i in range(k):
        for j in range(i+1,k):
            if (n-int(s[i])-int(s[j])) % 3 == 0:
                print(1)
                return
    print(-1)

if __name__ == '__main__':
    main()