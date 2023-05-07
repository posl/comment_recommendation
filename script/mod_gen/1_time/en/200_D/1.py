def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in range(n):
        b[a[i] % 200] += 1
    for i in range(200):
        if b[i] >= 2:
            print('Yes')
            print(b[i])
            for j in range(n):
                if a[j] % 200 == i:
                    print(j + 1, end = ' ')
                    b[i] -= 1
                    if b[i] == 0:
                        print()
                        break
            print(b[i])
            for j in range(n):
                if a[j] % 200 == i:
                    print(j + 1, end = ' ')
                    b[i] -= 1
                    if b[i] == 0:
                        print()
                        break
            return
    print('No')
main()

if __name__ == '__main__':
    main()