def main():
    n = int(input())
    for i in range(n):
        a = int(input())
        b = input().split()
        b = list(map(int, b))
        count = 0
        for j in range(a):
            if b[j] % 2 == 1:
                count += 1
        print(count)

if __name__ == '__main__':
    main()