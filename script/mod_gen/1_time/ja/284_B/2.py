def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        odd = 0
        for j in range(n):
            if a[j] % 2 == 1:
                odd += 1
        print(odd)

if __name__ == '__main__':
    main()